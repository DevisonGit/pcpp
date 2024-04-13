from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredDict created")

    def __getitem__(self, item):
        val = super().__getitem__(item)
        self.log_timestamp(f"value for key [{item}] retrieved")
        return val

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.log_timestamp(f"value for key [{key}]")

    def log_timestamp(self, message):
        timestamp_str = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f"{timestamp_str} {message}")


kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

print("Element kk[10]", kk[10])
print("whole dictionary", kk)
print("Our log book")
print("\n".join(kk.log))
