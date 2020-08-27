# This entrypoint file to be used in development. Start by reading README.md
import password_cracker
from unittest import main

# cracked_password1 = password_cracker.crack_sha1_hash(
#     "5d70c3d101efd9cc0a69f4df2ddf33b21e641f6a")
# print(cracked_password1)

# cracked_password2 = password_cracker.crack_sha1_hash(
#     "ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True)
# print(cracked_password2)

# # # Run unit tests automatically
main(module='test_module', exit=False)
