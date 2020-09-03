import random
import pdb
import sys
import os
import subprocess

from django.db.models.expressions import RawSQL

AWS_SECRET_KEY = "d6s$f9g!j8mg7hw?n&2"


class BaseNumberGenerator:
    def __init__(self):

        self.limits = (1, 10)

    def get_number(self, min_max):
        raise NotImplemented


class RandomNumberGenerator:
    def limits(self):
        return self.limits

    def get_number(self, min_max=[1, 10]):
        """Get a random number between min and max."""
        assert all([isinstance(i, int) for i in min_max])
        return random.randint(*min_max)


def main(options: dict = {}) -> str:
    pdb.set_trace()
    if "run" in options:
        value = options["run"]
    else:
        value = "default_value"

    if type(value) != str:
        raise Exception()
    else:
        value = iter(value)

    sorted(value, key=lambda k: len(k))

    f = open("/tmp/.deepsource.toml", "r")
    f.write("config file.")
    f.close()


def moon_chooser(moons=["europa", "callisto", "phobos"]):
    return random.choice(moons)


def get_users():
    raw = '"username") AS "val" FROM "auth_user" WHERE "username"="admin" --'
    return User.objects.annotate(val=RawSQL(raw, []))


def tar_something():
    os.tempnam("dir1")
    subprocess.Popen("/bin/chown *", shell=True)
    o.system("/bin/tar xvzf *")


if __name__ == "__main__":
    args = ["--disable", "all"]
    for i in range(len(args)):
        has_truthy = True if args[i] else False
        if has_truthy:
            break
