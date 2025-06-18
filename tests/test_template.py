import unittest
from unittest.mock import patch, Mock, mock_open
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.template import (
    get_python_download_url,
    get_cann_download_url,
    render_and_save_dockerfile,
    ALPHA_DICT
)

class TestTemplateFunctions(unittest.TestCase):
    
    @patch("tools.template.requests.get")
    def test_get_python_download_url(self, mock_get):
        mock_response = Mock()
        mock_response.text = """
            <a href="3.8.0/">3.8.0/</a>
            <a href="3.8.1/">3.8.1/</a>
            <a href="3.9.0/">3.9.0/</a>
        """
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        package, url, version = get_python_download_url("3.8")
        self.assertEqual(package, "Python-3.8.1")
        self.assertEqual(version, "3.8.1")
        self.assertIn("3.8.1", url)
        self.assertIn("repo.huaweicloud.com", url)
        
    def test_get_cann_download_url_alpha(self):
        version = "8.1.RC1.alpha001"
        chip = "310p"
        toolkit_url, kernels_url, nnal_url = get_cann_download_url(chip, version)
        self.assertIn(ALPHA_DICT[version], toolkit_url)
        self.assertIn("Milan-ASL", toolkit_url)
        self.assertIn("8.1.RC1.alpha001", toolkit_url)
        self.assertIn("310p", kernels_url)
        self.assertIn("Ascend-cann-nnal", nnal_url)
        
    def test_get_cann_download_url_release(self):
        version = "8.0.0"
        chip = "910b"
        toolkit_url, kernels_url, nnal_url = get_cann_download_url(chip, version)
        self.assertIn("CANN%208.0.0", toolkit_url)
        self.assertIn("Ascend-cann-toolkit", toolkit_url)
        self.assertIn("Ascend-cann-kernels", kernels_url)
        self.assertIn("Ascend-cann-nnal", nnal_url)
        
    @patch("tools.template.open", new_callable=mock_open)
    @patch("tools.template.os.makedirs")
    @patch("tools.template.get_python_download_url")
    @patch("tools.template.get_cann_download_url")
    @patch("tools.template.Environment")
    def test_render_and_save_dockerfile(self, mock_env, mock_get_cann, mock_get_py, mock_makedirs, mock_open_file):
        test_args = {
            "cann": [
                {
                    "os_name": "ubuntu",
                    "os_version": "22.04",
                    "py_version": "3.8",
                    "cann_chip": "910b",
                    "cann_version": "8.0.0"
                }
            ]
        }
        
        mock_get_py.return_value = ("Python-3.8.1", "http://python.url", "3.8.1")
        mock_get_cann.return_value = (
            "http://cann.toolkit.url",
            "http://cann.kernels.url",
            "http://cann.nnal.url"
        )
        
        mock_template = Mock()
        mock_template.render.return_value = "rendered dockerfile content"
        mock_env.return_value.get_template.return_value = mock_template
        render_and_save_dockerfile(test_args, "ubuntu.Dockerfile.j2", "openeuler.Dockerfile.j2")
        
        mock_get_py.assert_called_once_with("3.8")
        mock_get_cann.assert_called_once_with("910b", "8.0.0")
        mock_makedirs.assert_called_once()
        mock_open_file.assert_called_once()
        
        call_args = mock_open_file.call_args[0][0]
        self.assertIn("cann/8.0.0-910b-ubuntu22.04-py3.8/Dockerfile", call_args)
        

if __name__ == "__main__":
    unittest.main()