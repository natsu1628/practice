# [0, 0, 0, 0]
# [5, 0, 0, 0]
# [0, 0, 0, 0]
#
# snapdict -> key (snapid), value (dictionary)
# 1 -> {0: 5}
# 2 -> {}
#
# get(2) -> [0, 0, 0, 0]
# get(1) -> [5, 0, 0, 0]
#
#
# snapdict -> key (snapid), value (dictionary)
# 4 -> {0: 10, 2: 7}
# 3 -> {0: 5, 3: 8}
# 2 -> {1: 4}
# 1 -> {0: 10}
#
#
# check array - [T, T, T, T, F]
# Final array - [(10, 1), (4, 1), 7, 8, 0] -> [ (actual value, flag) ]
# flag -> 0 (this index value can be changed)
# flag -> 1 (this index value cannot be changed)
# O(nk)
# O(n) -> best space complexity



class SnapshotArray:
    def __init__(self, length):
        self.snapshot = [0 for _ in range(length)]
        self.snapdict = dict()
        self.snapid = 0

    def set(self, index, val):
        if index >= len(self.snapshot):
            print("Array Index out of bounds")
            return
        self.snapshot[index] = val

    def snap(self):
        self.snapid += 1
        self.snapdict[self.snapid] = dict()
        for index in range(len(self.snapshot)):
            if self.snapshot[index] != 0:
                self.snapdict[self.snapid][index] = self.snapshot[index]
        return self.snapid

    def get(self, snap_id):
        if snap_id not in self.snapdict:
            print(f"Snap id: {snap_id} not present")
            return None
        tmp = [0 for _ in range(len(self.snapshot))]
        value_dict = self.snapdict[snap_id]
        for k, v in value_dict.items():
            tmp[k] = v
        return tmp


if __name__ == "__main__":
    sn = SnapshotArray(4)
    sn.set(0, 5)
    id = sn.snap()
    # print(id)
    print(sn.get(1))
    print(sn.get(2))
    sn.set(0, 0)
    sn.set(2, 100)
    sn.set(1, 89)
    id = sn.snap()
    sn.snap()
    sn.snap()
    sn.set(4, 5)
    sn.snap()
    # print(id)
    # print(sn.snap())
    # print(sn.snap())
    print(sn.get(5))



