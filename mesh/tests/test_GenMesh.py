"""test_GenMesh.py

Copyright 2016 Mark L. Palmeri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

xyz = (0, 2, 3, 5, 6, 8)
numElem = (2, 2, 2)
pos = [[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
header_comment = "$Generated by test_GenMesh.py"


def test_calc_node_pos():
    """calculate unique x, y, z positions for the mesh
    """
    from GenMesh import calc_node_pos
    assert calc_node_pos(xyz, numElem) == pos


def test_check_x0_y0():
    """do not pass if 0.0 missing from x or y
    """

    from GenMesh import check_x0_y0
    assert check_x0_y0(pos) != 1

    pos2 = pos
    pos2[1][1] = 0.0
    assert check_x0_y0(pos2) == 0


def test_writeNodes(tmpdir):
    """write test nodes.dyn file
    """
    from GenMesh import writeNodes

    nodefile = "nodes.dyn"
    f = tmpdir.join(nodefile)
    writeNodes(pos, f.strpath, header_comment)
    lines = f.readlines()
    assert lines[0] == header_comment+"\n"
    assert lines[1] == "*NODE\n"
    assert lines[2] == "1,0.000000,3.000000,6.000000\n"
    assert lines[-1] == "*END\n"


def test_writeElems(tmpdir):
    """write test elems.dyn file
    """
    from GenMesh import writeElems

    elefile = "elems.dyn"
    partid = 1
    f = tmpdir.join(elefile)
    writeElems(numElem, partid, f.strpath, header_comment)
    lines = f.readlines()
    assert lines[0] == header_comment+"\n"
    assert lines[1] == "*ELEMENT_SOLID\n"
    assert lines[2] == "1,1,1,2,5,4,10,11,14,13\n"
    assert lines[-1] == "*END\n"