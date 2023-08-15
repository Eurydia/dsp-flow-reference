import urllib.parse


# class IconMode:
#     ONE_LARGE: str = "10"

#     @staticmethod
#     def from_string(key: str) -> str:
#         DICT: dict[str, str] = {
#             "10": "One large",
#             "11": "One small",
#         }
#         return DICT[key]


class Blueprint:
    def __init__(self, content: str) -> None:
        self.__content = content.split(",")

    # @property
    # def name(self) -> str:
    #     return self.__content[10]

    # @property
    # def desc(self) -> str:
    #     desc_content: str = ""
    #     for char in self.__content[11]:
    #         if char == '"':
    #             return desc_content
    #         desc_content += char

    def set_name(self, name: str) -> None:
        self.__content[10] = urllib.parse.quote(name)

    def set_desc(self, desc: str) -> None:
        index: int = self.__content[11].find('"')

        attached_desc: str = (
            urllib.parse.quote(desc) + self.__content[11][index:]
        )
        self.__content[11] = attached_desc

    @property
    def as_string(self) -> str:
        return ",".join(self.__content)


desc: str = """ss
"""


def main() -> None:
    bp: Blueprint = Blueprint(
        r'BLUEPRINT:0,10,1101,0,0,0,0,0,638271948455121690,0.9.27.15466,Iron%20Ingot%20A,"H4sIAAAAAAAAC5WXTWhcVRTH75tJM9Pma1LTJJMmncTE1JpaY8x0prHJvDeBim6cZZfZ6EbBiBbcJbiwgojZSP3CICgEPzC0aSedCo0IpVQpbV120Qoi2EWLYNFoJs973rn3zj/jQeKDd98/L/zOOf977zu58ZRSzfqOKb669b3DaE+FSl02r3eoonmtNsNTwef7M1lv9vnyVn2mSPf1xGAUI9SXR2FcPH3F1QIBZ72P0quoqxqsGlgJcIyHJZcNNWZuEOA4p191AOru6pki3QSH5lIAN/Bj2QFb9UqRboLjQuZoLqvhogNQexr0DBwT4EaeiJMOQB3XYNzAngAneMJmgsh7/sfyVr1SjBl4lwAn2fi8y4YaPTcK8E4a/goLDkCNmZsFeBcv1awrFfWGXuMNs85JAW5iz/1uV6HGTdImwM2cuQTLUxI9JwS4hR+3/RqAuga3CnCrWWyXDTXCuwW4jTf4qJsk1Oh5pwCneKkWudS19DnUmLldgNt5ttccgBq/5xYBJiv660i5UlFj2U0C/AANf4e3fP1t+t7lL3Oov3m9eJruzeQUfs+KeY7RQQP1rpia972FdA61Uien6absnUL2PRxrngHtFTXC+wS4kx8LACyIcLcAd9FAHcSWihrhDgHu5uV6M/AIiD7FmkZ4jwCneYuWHIAa4QEB7uHHMvhcFj33CvBeFb0sOwD1zfCNaboJ7hHgXn4sQbYlMXOXAPfxIwVASoQHBXgfb5JZN0moEe4X4Ax7zoDnjJi5T4D7eZ1nYJ1nxMxpAR5g2HfZUCP8oADTu6gV2WyoEc4I8CBPmIIJUyI8JMBD/Ljt1z4G1DX4IQGmd/qruuhbn6gRPirAwzR8otvPu79dKn/7/nSFWtE7kx8UXh4eufDV2ND5g69l8jcTB6KeRY0wEfLBimJQlP229MmfxnyC2rS+G875FKz1u/GzV0+kogDkkYLo9B43NA7wMAegL0oZv6j5+q9meEBFpS0HN+58ry0cq1AAa6Hp0Kf5zmI6qoAyNVgLUMEjtgJr4ffw68Ba+PXPU9lrnV/kKECPKTf0tgYYYfmeKxv1diwcpGFD93BrgQK8TRZ+Gbnww1ut5wdO7I4sjJhg9avwqFJ84LEWNsO54F5kwa+8NDW6MpFORRaoOY4JFg5ZC0cpgM76h67GBlhs/zjb0rUWBegwfusDPKaiX5SCtp+vaQtPV+Ja21VIP3M/P5jkjZRVfFapX4VRkk3agt2JZMcGeG74eq63jwNQ+UkhwOMk6cRk5+C+7jp2GZ965cOVz/YeP0cB6PMdFyyMsZwP7J9i1NtZxid4FfrdHFDfsxZO37qyWmgciCyMKz7s1Vug96Zx8uZBvZ0KsvxjCXZi6X8FOEwDLZ3dB+vhs2YSj1XW+17I3nn1xTJZSJts9ZOYM5PoTlKo8WCUUv/uRnkaqmEBjmEF8TyXE+AjNNwLw0JUge66qBHOC/AEw3MA1zSWfUSAn6RBl3nYlooaM08IMHXl6AxrWzZqbN+TAkzv1Lpenpj5S4Ma4SkBnrKzbQHUCBcEuGBn2wKoEfYF2LezXYPnRDgQ4MCKGoC6Bkv/Df8DosYhpDEQAAA="8627B221D98CF6437D04E7EBA6D05AB4'
    )
    bp.set_name("Iron Ingot")

    bp.set_desc(
        """sdsd
"""
    )

    with open("helper/out.txt", "w+", encoding="utf-8") as f:
        print(bp.as_string, file=f)


if __name__ == "__main__":
    main()