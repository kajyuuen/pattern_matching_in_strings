from typing import List


class BruteForceSearcher:
    @classmethod
    def search(cls,
               text: str,
               pattern: str) -> List[int]:
        match_indexes = []
        n = len(text)
        m = len(pattern)

        for i in range(n-m-1):
            flag = True
            for j in range(m):
                if text[i+j] != pattern[j]:
                    flag = False
                    break
            if flag:
                match_indexes.append(i)

        return match_indexes

if __name__ == "__main__":
    assert [2, 5] == BruteForceSearcher.search("ababcabcabcc", "abcab")
