class Solution:
    # def compareVersion(self, version1: str, version2: str) -> int:
    #     version1 = [int(i) for i in version1.split('.')]
    #     version2 = [int(i) for i in version2.split('.')]
    #     rev = 1
    #     if len(version2) < len(version1):
    #         version1, version2 = version2, version1
    #         rev = -1
    #     for i in range(len(version1)):
    #         if version1[i] > version2[i]:
    #             return rev
    #         elif version1[i] < version2[i]:
    #             return -rev
    #     i += 1
    #     while i < len(version2):
    #         if version2[i] > 0:
    #             return -rev
    #         i += 1
    #     return 0

    # A more concise version
    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1), len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

if __name__ == '__main__':
    print(Solution().compareVersion(version1="1.0", version2="1"))
