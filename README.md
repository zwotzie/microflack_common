MicroFlack's Common Package
===========================

mkwheel script builds a wheel for the package and adds it to the wheel directory

export WHEELHOUSE=?? <- must be set, there the microflack_comman package is copied to

* To build the latest version, invoke it without arguments: ./mkwheel
* To build a specific version, pass the git tag for that version: ./mkwheel 0.1
* To build all versions, pass "all" as argument: ./mkwheel all

# when used by a container:
docker in container.py needs the option *--volume=/var/run/docker.sock:/var/run/docker.sock* in "docker run",
