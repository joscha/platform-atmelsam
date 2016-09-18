from platformio.managers.platform import PlatformBase


class SodaqsamdPlatform(PlatformBase):

    def configure_default_packages(self, variables, targets):
        if variables.get("board"):
            upload_protocol = self.board_config(variables.get("board")).get(
                "upload.protocol", "")
            upload_tool = None
            if upload_protocol == "sam-ba":
                upload_tool = "tool-bossac"

            if upload_tool:
                for name, opts in self.packages.items():
                    if "type" not in opts or opts['type'] != "uploader":
                        continue
                    if name != upload_tool:
                        del self.packages[name]

        return PlatformBase.configure_default_packages(
            self, variables, targets)
