import math;
import random;
import os;

# Path for the output directory; must exist before the program is started. You should change it to your desired path.
filepath = "c:\\_preklad\\_knihy\\hyperrogue\\euclidean\\";
listfile = "eusolver_";
genfile = "euoutput";

# This constant sets the maximum number of vertices that a solution may contain.
maxnum = 12;

# These arrays initialize all the vertex types the program works with.
symbollist = ["(3,12,12)A","(3,12,12)F","(4,6,12)","(6,6,6)S","(6,6,6)R","(6,6,6)A","(6,6,6)F","(3,3,4,12)","(3,4,3,12)A","(3,4,3,12)F","(3,3,6,6)A","(3,3,6,6)F","(3,6,3,6)S","(3,6,3,6)R","(3,6,3,6)A1","(3,6,3,6)A2","(3,6,3,6)F","(3,4,4,6)","(3,4,6,4)A","(3,4,6,4)F","(4,4,4,4)S4","(4,4,4,4)R4","(4,4,4,4)S2a","(4,4,4,4)S2b","(4,4,4,4)R2","(4,4,4,4)A1","(4,4,4,4)A2","(4,4,4,4)F","(3,3,3,3,6)A","(3,3,3,3,6)F","(3,3,3,4,4)A","(3,3,3,4,4)F","(3,3,4,3,4)A","(3,3,4,3,4)F","(3,3,3,3,3,3)S6","(3,3,3,3,3,3)R6","(3,3,3,3,3,3)S3a","(3,3,3,3,3,3)S3b","(3,3,3,3,3,3)R3","(3,3,3,3,3,3)S2","(3,3,3,3,3,3)R2","(3,3,3,3,3,3)A1","(3,3,3,3,3,3)A2","(3,3,3,3,3,3)F"];

labellistin = [["0","1","*0"],["0","1","2","*0","*1","*2"],["0","1","2","*0","*1","*2"],["0"],["0","*0"],["0","1","*1"],["0","1","2","*0","*1","*2"],["0","1","2","3","*0","*1","*2","*3"],["0","*0","2","*2"],["0","1","2","3","*0","*1","*2","*3"],["0","1","*0","3"],["0","1","2","3","*0","*1","*2","*3"],["0","*0"],["0","1","*0","*1"],["0","1","*1","*0"],["0","*0","2","*2"],["0","1","2","3","*0","*1","*2","*3"],["0","1","2","3","*0","*1","*2","*3"],["0","*0","2","*2"],["0","1","2","3","*0","*1","*2","*3"],["0"],["0","*0"],["0","1"],["0","*0"],["0","1","*0","*1"],["0","1","2","*1"],["0","*0","2","*2"],["0","1","2","3","*0","*1","*2","*3"],["0","*0","2","3","*2"],["0","1","2","3","4","*0","*1","*2","*3","*4"],["0","1","*0","3","*3"],["0","1","2","3","4","*0","*1","*2","*3","*4"],["0","1","*1","*0","4"],["0","1","2","3","4","*0","*1","*2","*3","*4"],["0"],["0","*0"],["0","1"],["0","*0"],["0","1","*0","*1"],["0","1","*1"],["0","1","2","*0","*1","*2"],["0","1","2","3","*2","*1"],["0","1","2","*2","*1","*0"],["0","1","2","3","4","5","*0","*1","*2","*3","*4","*5"]];

lneiglistin = [[2,0,1],[2,0,1,4,5,3],[2,0,1,4,5,3],[0],[0,1],[2,0,1],[2,0,1,4,5,3],[3,0,1,2,5,6,7,4],[3,0,1,2],[3,0,1,2,5,6,7,4],[3,0,1,2],[3,0,1,2,5,6,7,4],[1,0],[1,0,3,2],[3,0,1,2],[3,0,1,2],[3,0,1,2,5,6,7,4],[3,0,1,2,5,6,7,4],[3,0,1,2],[3,0,1,2,5,6,7,4],[0],[0,1],[1,0],[1,0],[1,0,3,2],[3,0,1,2],[3,0,1,2],[3,0,1,2,5,6,7,4],[4,0,1,2,3],[4,0,1,2,3,6,7,8,9,5],[4,0,1,2,3],[4,0,1,2,3,6,7,8,9,5],[4,0,1,2,3],[4,0,1,2,3,6,7,8,9,5],[0],[0,1],[1,0],[1,0],[1,0,3,2],[2,0,1],[2,0,1,4,5,3],[5,0,1,2,3,4],[5,0,1,2,3,4],[5,0,1,2,3,4,7,8,9,10,11,6]];

rneiglistin = [[1,2,0],[1,2,0,5,3,4],[1,2,0,5,3,4],[0],[0,1],[1,2,0],[1,2,0,5,3,4],[1,2,3,0,7,4,5,6],[1,2,3,0],[1,2,3,0,7,4,5,6],[1,2,3,0],[1,2,3,0,7,4,5,6],[1,0],[1,0,3,2],[1,2,3,0],[1,2,3,0],[1,2,3,0,7,4,5,6],[1,2,3,0,7,4,5,6],[1,2,3,0],[1,2,3,0,7,4,5,6],[0],[0,1],[1,0],[1,0],[1,0,3,2],[1,2,3,0],[1,2,3,0],[1,2,3,0,7,4,5,6],[1,2,3,4,0],[1,2,3,4,0,9,5,6,7,8],[1,2,3,4,0],[1,2,3,4,0,9,5,6,7,8],[1,2,3,4,0],[1,2,3,4,0,9,5,6,7,8],[0],[0,1],[1,0],[1,0],[1,0,3,2],[1,2,0],[1,2,0,5,3,4],[1,2,3,4,5,0],[1,2,3,4,5,0],[1,2,3,4,5,0,11,6,7,8,9,10]];

mirrolistin = [[2,1,0],[3,4,5,0,1,2],[3,4,5,0,1,2],[0],[1,0],[0,2,1],[3,4,5,0,1,2],[4,5,6,7,0,1,2,3],[1,0,3,2],[4,5,6,7,0,1,2,3],[2,1,0,3],[4,5,6,7,0,1,2,3],[1,0],[2,3,0,1],[3,2,1,0],[1,0,3,2],[4,5,6,7,0,1,2,3],[4,5,6,7,0,1,2,3],[1,0,3,2],[4,5,6,7,0,1,2,3],[0],[1,0],[0,1],[1,0],[2,3,0,1],[0,3,2,1],[1,0,3,2],[4,5,6,7,0,1,2,3],[1,0,4,3,2],[5,6,7,8,9,0,1,2,3,4],[2,1,0,4,3],[5,6,7,8,9,0,1,2,3,4],[3,2,1,0,4],[5,6,7,8,9,0,1,2,3,4],[0],[1,0],[0,1],[1,0],[2,3,0,1],[0,2,1],[3,4,5,0,1,2],[0,5,4,3,2,1],[5,4,3,2,1,0],[6,7,8,9,10,11,0,1,2,3,4,5]];

lvertlistin = [[3,12,12],[3,12,12,12,12,3],[4,12,6,12,6,4],[6],[6,6],[6,6,6],[6,6,6,6,6,6],[3,12,4,3,12,4,3,3],[3,12,3,4],[3,12,3,4,12,3,4,3],[3,6,6,3],[3,6,6,3,6,6,3,3],[3,6],[3,6,6,3],[3,6,3,6],[3,6,3,6],[3,6,3,6,6,3,6,3],[3,6,4,4,6,4,4,3],[4,6,4,3],[4,6,4,3,6,4,3,4],[4],[4,4],[4,4],[4,4],[4,4,4,4],[4,4,4,4],[4,4,4,4],[4,4,4,4,4,4,4,4],[3,6,3,3,3],[3,6,3,3,3,6,3,3,3,3],[3,4,4,3,3],[3,4,4,3,3,4,4,3,3,3],[3,4,3,4,3],[3,4,3,4,3,4,3,4,3,3],[3],[3,3],[3,3],[3,3],[3,3,3,3],[3,3,3],[3,3,3,3,3,3],[3,3,3,3,3,3],[3,3,3,3,3,3],[3,3,3,3,3,3,3,3,3,3,3,3]];

# This assigns a code to each vertex type. These are used to make the filenames shorter.
codelist = ["3a","3b","3c","3d","3e","3f","3g","4a","4b","4c","4d","4e","4f","4g","4h","4i","4j","4k","4l","4m","4n","4o","4p","4q","4r","4s","4t","4u","5a","5b","5c","5d","5e","5f","6a","6b","6c","6d","6e","6f","6g","6h","6i","6j"];

# These lists are used to store various informations about the partial solutions.
labellist = [];
lneiglist = [];
rneiglist = [];
mirrolist = [];
lvertlist = [];
gluelist = [];
numlist = [];
vertypelist = [];

# This keeps tally of the various solution types and their numbers.
runtotal1 = [];
runtotal2 = [];

# And this keeps tally of vertex combinations that have solutions and the number of that solutions.
vertypesolved = [];
vertypesolvedcount = [];

# These two keep tally of the total number of partial solutions checked and of total number of solutions found.
solcount = 0;
solfound = 0;

# A basic function that gives a text representation of an edge x of tile y.
def edgelabel(edge,tile):
  m = str(edge);
  if tile > 3:
    m = m + "@" + str(tile);
  else:
    for i in range(tile):
      m = m + "'";
  return(m);

# This function expresses the pairing of two edges as easy-to-read Conway symbol.
def conwaysymbol(first, second):
  mirrornum = 0;
  if first[0] == "*":
    mirrornum += 1;
    first = first[1:];
  if second[0] == "*":
    mirrornum += 1;
    second = second[1:];
  same = first == second;
  if mirrornum != 1:
    if same:
      return "(" + first + ")";
    else:
      return "(" + first + " " + second + ")";
  else:
    if same:
      return "[" + first + "]";
    else:
      return "[" + first + " " + second + "]";

# This function creates a complete Conway symbol from a gluing.
def writeconway(mirro,glue,label):
  smet = [];
  conwaystring = "";
  for cy in range(len(glue)):
    if not cy in smet and glue[cy] != -1:
      first = label[cy];
      second = label[glue[cy]];
      smet.append(cy);
      smet.append(glue[cy]);
      smet.append(mirro[cy]);
      smet.append(glue[mirro[cy]]);
      conwaystring = conwaystring + conwaysymbol(first,second);
  return conwaystring;

# Another ourput function: this one takes a list of vertex configurations in a tiling and uses their symbols (from symbollist) to express them in a readable form.
def verbalvertices(vertype):
  s = "";
  for i in vertype:
    s = s + symbollist[i] + ", ";
  return s[:-2];

# One of the key functions. It looks through a partial solution and verifies its legality. A solution can fail on three counts:
# 1) It contains mismatched corners. Each corner knows which polygon it belongs to (defined in the lvert array). All corners of the same polygon must have this property set to the same value.
# 2) It contains overly large polygons. If the number of corners of a polygon exceeds its value (for example if a hexagon is found to have 7 vertices), the partial solution is invalid.
# 3) It contains completed polygons of wrong size. If the polygon is complete (last corner is connected to the first one), its size must be a divisor of the true size. For example, a hexagon may be formed by not just by a cycle of 6 corners, but also by a cycle of 3, 2, or just 1. But a completed hexagon with 5 corners is wrong.
def checkpart(rneig, lneig, lvert, mirro, glue):
  for i in range(len(rneig)):
    free = i;
    rfree = rneig[free];
    vfree = lvert[rfree];
    mainvert = vfree;
    count = 1;
    passt = False;
    fail = False;
    while (not passt and not fail):
      free = glue[rfree];
      if free == -1:
        if count > mainvert:
          fail = True;
        else:
          passt = True;
      elif free == i:
        if mainvert % count != 0:
          fail = True;
        else:
          passt = True;
      else:
        rfree = rneig[free];
        vfree = lvert[rfree];
        count += 1;
#        if count > 100:
#          print(rneig, lneig, lvert, mirro, glue);
        if vfree != mainvert:
          fail = True;
    if fail:
      return False;
  return True;

# This function is used to write down the polygon cycles of the current partial solution. However, it has an important secondary purpose as well -- it sets the global variable mincycle, which is used to pick the edge that will be extended. Currently, it finds the "tightest" partial polygon -- i.e. the one which is closest to reaching its maximum size -- and tries to extend an edge at one of its ends. In particular, if a polygon has its maximum size but is not completed, this will force an extension that tries to tie its ends together.
def writecycle(rneig,lneig,lvert,glue,label,filen):
  global mincycle;
  mincycle = [-1,13];
  v = 0;
  smet = [];
  for cy in range(len(glue)):
    mainst = ""
    count = 0;
    complete = False;
    if not cy in smet:
      left = cy;
      while glue[left] != -1 and glue[left] != rneig[cy]:
        left = lneig[glue[left]];
      if (glue[left]==-1):
        stable = left;
        right = rneig[left];
        vstable = lvert[right];
        cont = True;
        while cont:
          smet.append(left);
          mainst = mainst + label[left] + "/" + label[right] + "(" + str(lvert[right]) + ")-";
          count += 1;
          left = glue[right];
          if left != -1:
            right = rneig[left];
          else:
            dif = vstable - count;
            if dif < mincycle[1]:
              mincycle = [stable,dif];
            cont = False;
      else:
        left = cy;
        right = rneig[left];
        v = lvert[right];
        cont = True;
        complete = True;
        while cont:
          smet.append(left);
          mainst = mainst + label[left] + "/" + label[right] + "(" + str(lvert[right]) + ")-";
          count += 1;
          left = glue[right];
          if left != cy:
            right = rneig[left];
          else:
            cont = False;
      if complete:
        mainst = mainst[:-1];
        ratio = int(v/count);
        if ratio != 1:
          mainst = " [" + mainst + "]x" + str(ratio);
        else:
          mainst = " " + mainst;
      filen.write(mainst+"\n");

# Just a simple routine for output of lists. Currently not used anymore.
def listwrite(l):
  s = "[";
  for i in l:
    s = s + str(i) + ",";
  return s[:-1]+"]";

# These two functions together allow to create "signatures". Signatures are another way to express the set of vertices in the tiling; this time the vertices are ordered and identical vertices are grouped together into one symbol. This makes signatures easier to read than full vertex lists. All solutions with the same set of vertices will have the same signature, even if the actual order of added vertices is different, and since signature is written into the output files, it makes it easy to search for all solutions with a given set.
def sig(result):
  s = "";
  for i in range(len(result)):
    if result[i] > 0:
      s = s + symbollist[i];
      if result[i] > 1:
        s = s + "x" + str(result[i]);
      s = s + ", ";
  return s[:-2];

def signature(vertype):
  result = [];
  for i in range(len(symbollist)):
    result.append(0);
  for i in vertype:
    result[i] += 1;
  return sig(result);

# This is a similar concept to signature, except with the vertex codes. It's used to create the filenames.
def filesignature(vertype):
  result = [];
  for i in range(len(symbollist)):
    result.append(0);
  for i in vertype:
    result[i] += 1;
  s = "";
  for i in range(len(result)):
    if result[i] > 0:
      s = s + codelist[i];
      if result[i] > 1:
        s = s + str(result[i]);
      s = s + " ";
  return s[:-1];

# This adds a solution into vertypesolved -- either appending it, if new, or just increasing the count for that particular set of vertices.
def vertypesolvedadd(vertype):
  global vertypesolved,vertypesolvedcount;
  s = [];
  result = [];
  for i in range(symbolcount):
    result.append(0);
  for i in vertype:
    result[i] += 1;
  if not result in vertypesolved:
    vertypesolved.append(result);
    vertypesolvedcount.append(1);
    x = len(vertypesolved)-1;
  else:
    x = vertypesolved.index(result);
    vertypesolvedcount[x] += 1;
  return x;

# This function creates the initial set of partial solutions to be extended. It creates one partial solution for each vertex type, consisting of just the vertex.
def initex():
  for i in range(len(symbollist)):
    labellist.append(labellistin[i]);
    lneiglist.append(lneiglistin[i]);
    rneiglist.append(rneiglistin[i]);
    mirrolist.append(mirrolistin[i]);
    lvertlist.append(lvertlistin[i]);
    vertypelist.append([i]);
    numlist.append(1);
    glue = [];
    for j in range(len(lneiglistin[i])):
      glue.append(-1);
    gluelist.append(glue);

# This is an attempt to limit duplicates a bit; certain vertex configurations have multiple equivalent ways to be attached. For example, a vertex (3,3,6,6)F can be attached in 8 ways (4 edges for either normal or mirror version), but if we add it as a new vertex, it should be always added in "normal" orientation since the other way doesn't bring anything new. This function thus limits the amount of possible attachments for vertices with lesser than nominal symmetry.
def ferk(x):
  t = symbollist[x];
  q = len(lneiglistin[x]);
  if t in ["(3,12,12)F","(6,6,6)R","(3,4,3,12)F","(3,3,6,6)F","(3,6,3,6)R","(3,4,6,4)F","(4,4,4,4)R4","(4,4,4,4)S2a","(4,4,4,4)S2b","(4,4,4,4)A1","(3,3,3,3,6)F","(3,3,3,4,4)F","(3,3,4,3,4)F","(3,3,3,3,3,3)R6","(3,3,3,3,3,3)S3a","(3,3,3,3,3,3)S3b","(3,3,3,3,3,3)A1","(3,3,3,3,3,3)A2"]:
    q = int(q/2);
  elif t in ["(3,6,3,6)F","(4,4,4,4)R2","(4,4,4,4)A2","(3,3,3,3,3,3)R3"]:
    q = int(q/4);
  elif t in ["(6,6,6)F","(3,3,3,3,3,3)R2"]:
    q = int(q/6);
  elif t == "(4,4,4,4)F":
    q = int(q/8);
  elif t == "(3,3,3,3,3,3)F":
    q = int(q/12);
  return q;

# Just a way to add leading zero to numbers in order to pad them to the same length.
def fname(num):
  m = str(num);
  if num < 10:
    m = "0"+m;
  return m;

# This creates a code noting the types of polygons present in the solution.
def finename(lvert,num):
  m = fname(num)+"_";
  if 3 in lvert:
    m = m + "3";
  if 4 in lvert:
    m = m + "4";
  if 6 in lvert:
    m = m + "6";
  if 12 in lvert:
    m = m + "c";
  return m;

# The main output: writes a *.tes file, ready for use in HyperRogue.
def teswrite(conway,polysizelist,repeatlist,tesfile,solstring):
  tes = open(tesfile,"w");
  tes.write("## Euclidean, "+solstring+"\n");
  tes.write("e2.\n");
  tes.write("angleunit(deg)\n");
  for i in polysizelist:
    tes.write("unittile(");
    polysec = "";
    for j in range(i):
      polysec = polysec + str(180-int(360/i)) + ",";
    tes.write(polysec[:-1]+")\n");
  tes.write("conway(\""+conway+"\")\n");
  for i in range(len(repeatlist)):
    if repeatlist[i] > 1:
      tes.write("repeat("+str(i)+","+str(repeatlist[i])+")\n");
  tes.close();

# This pair of functions transforms the original solution (which is vertex-based) into tile-based representation. This is necessary to display it in HyperRogue. There are two functions based on whether the solution contains axially symmetrical tiles, as these need to be considered in different ways.
def assemblechiral(oldmainstlist,oldrepeatlist,filen,tesfile,solstring):
  leftedges=[];
  rightedges=[];
  edges=[];
  polysizelist=[];
  conway = "";
  half = math.floor(len(oldmainstlist)/2);
  mainstlist = [];
  repeatlist = [];
  for cut in range(half):
    mainstlist.append(oldmainstlist[2*cut]);
    repeatlist.append(oldrepeatlist[2*cut]);
  for m in range(len(mainstlist)):
    mainst = mainstlist[m];
    rep = repeatlist[m];
    if rep > 1:
      xi = mainst.index("]");
      mainst = mainst[1:xi];
    ind1 = mainst.index("(");
    ind2 = mainst.index(")");
    size = int(mainst[ind1+1:ind2]);
    polysizelist.append(size);
    mainst = mainst+"-";
    rev = len(mainst)-1;
    while mainst[rev] != "/":
      rev -= 1;
    mainst = mainst[rev+1:]+mainst[:rev+1];
    edgeindex = 0;
    while len(mainst) > 0:
      ind = mainst.index("/");
      chunk = mainst[:ind+1];
      mainst = mainst[ind+1:];
      ind = chunk.index("(");
      leftedges.append(chunk[:ind]);
      ind = chunk.index("-");
      rightedges.append(chunk[ind+1:-1]);
      edges.append(edgelabel(edgeindex,m));
      edgeindex += 1;
  while len(leftedges) > 0:
    if rightedges.count(leftedges[0]) > 0:
      match = rightedges.index(leftedges[0]);
      if match == 0:
        conway = conway + "(" + edges[0] + ")";
        del(leftedges[0]);
        del(rightedges[0]);
        del(edges[0]);
      else:
        conway = conway + "(" + edges[0] + " " + edges[match] + ")";
        del(leftedges[match]);
        del(rightedges[match]);
        del(edges[match]);
        del(leftedges[0]);
        del(rightedges[0]);
        del(edges[0]);
    else:
      if leftedges[0][0] == "*":
        mirrormatch = leftedges[0][1:];
      else:
        mirrormatch = "*"+leftedges[0];
      if leftedges.count(mirrormatch) > 0:
        match = leftedges.index(mirrormatch);
      else:
        match = 0;
      if match == 0:
        conway = conway + "[" + edges[0] + "]";
        del(leftedges[0]);
        del(rightedges[0]);
        del(edges[0]);
      else:
        conway = conway + "[" + edges[0] + " " + edges[match] + "]";
        del(leftedges[match]);
        del(rightedges[match]);
        del(edges[match]);
        del(leftedges[0]);
        del(rightedges[0]);
        del(edges[0]);
  filen.write(conway+"\n");
  teswrite(conway,polysizelist,repeatlist,tesfile,solstring);

def assembleachiral(mainstlist,repeatlist,filen,tesfile,solstring):
  leftedges=[];
  rightedges=[];
  edges=[];
  polysizelist=[];
  conway = "";
  for m in range(len(mainstlist)):
    mainst = mainstlist[m];
    rep = repeatlist[m];
    if rep > 1:
      xi = mainst.index("]");
      mainst = mainst[1:xi];
    ind1 = mainst.index("(");
    ind2 = mainst.index(")");
    size = int(mainst[ind1+1:ind2]);
    polysizelist.append(size);
    mainst = mainst+"-";
    rev = len(mainst)-1;
    while mainst[rev] != "/":
      rev -= 1;
    mainst = mainst[rev+1:]+mainst[:rev+1];
    edgeindex = 0;
    while len(mainst) > 0:
      ind = mainst.index("/");
      chunk = mainst[:ind+1];
      mainst = mainst[ind+1:];
      ind = chunk.index("(");
      leftedges.append(chunk[:ind]);
      ind = chunk.index("-");
      rightedges.append(chunk[ind+1:-1]);
      edges.append(edgelabel(edgeindex,m));
      edgeindex += 1;
  while len(leftedges) > 0:
    match = rightedges.index(leftedges[0]);
    if match == 0:
      conway = conway + "(" + edges[0] + ")";
      del(leftedges[0]);
      del(rightedges[0]);
      del(edges[0]);
    else:
      conway = conway + "(" + edges[0] + " " + edges[match] + ")";
      del(leftedges[match]);
      del(rightedges[match]);
      del(edges[match]);
      del(leftedges[0]);
      del(rightedges[0]);
      del(edges[0]);
  filen.write(conway+"\n");
  teswrite(conway,polysizelist,repeatlist,tesfile,solstring);

# Unlike writecycle, which is used for partial solutions, this function is used only when a solution is actually found. It gives that solution a full treatment, including transformation into tile-based representation and creating a *.tes file.
def writecyclefinal(rneig,lneig,lvert,mirro,glue,label,filen,tesfile,solstring):
  v = 0;
  smet = [];
  mainstlist = [];
  sublist = [];
  ultrachiral = True;
  repeatlist = [];
  for cy in range(len(glue)):
    mainst = ""
    count = 0;
    complete = False;
    minmirror = len(glue);
    if not cy in smet:
      left = cy;
      right = rneig[left];
      v = lvert[right];
      cont = True;
      while cont:
        smet.append(left);
        if mirro[right] < minmirror:
          minmirror = mirro[right];
        mainst = mainst + label[left] + "/" + label[right] + "(" + str(lvert[right]) + ")-";
        count += 1;
        left = glue[right];
        if left != cy:
          right = rneig[left];
        else:
          cont = False;
      mainst = mainst[:-1];
      ratio = math.floor(v/count);
      repeatlist.append(ratio);
      if ratio != 1:
        mainst = "[" + mainst + "]x" + str(ratio);
      mainstlist.append(mainst);
      if minmirror in smet:
        sublist.append(0);
        ultrachiral = False;
      else:
        left = minmirror;
        mainst = "";
        right = rneig[left];
        v = lvert[right];
        cont = True;
        while cont:
          smet.append(left);
          mainst = mainst + label[left] + "/" + label[right] + "(" + str(lvert[right]) + ")-";
          count += 1;
          left = glue[right];
          if left != minmirror:
            right = rneig[left];
          else:
            cont = False;
        mainst = mainst[:-1];
        repeatlist.append(ratio);
        if ratio != 1:
          mainst = "[" + mainst + "]x" + str(ratio);
        mainstlist.append(mainst);
        sublist = sublist + [1,2];
  for m in range(len(mainstlist)):
    mainst = mainstlist[m];
    sub = sublist[m];
    if sub == 0:
      filen.write(str(m)+": "+mainst);
    elif sub == 1:
      if not ultrachiral:
        header = str(m)+"/"+str(m+1)+": ";
      else:
        header = str(math.floor(m/2))+": ";
      subheader = "";
      for s in range(len(header)):
        subheader = subheader + " ";
      filen.write(header+mainst);
    else:
      filen.write(subheader+mainst);
    filen.write("\n");
  filen.write("---\n");
  if ultrachiral:
    assemblechiral(mainstlist,repeatlist,filen,tesfile,solstring);
  else:
    assembleachiral(mainstlist,repeatlist,filen,tesfile,solstring);

# Since the number of solutions may be large, the script builds a directory structure to make the size of individual directories manageable. This function checks whether the specified path exists, and if not, creates the necessary directories.
def checkdirectory(finn,fine,filesig):
  if not os.path.exists(filepath + finn + "\\"):
     os.makedirs(filepath + finn + "\\")
  if not os.path.exists(filepath + finn + "\\" + fine + "\\"):
     os.makedirs(filepath + finn + "\\" + fine + "\\")
  if not os.path.exists(filepath + finn + "\\" + fine + "\\" + filesig + "\\"):
     os.makedirs(filepath + finn + "\\" + fine + "\\" + filesig + "\\")

# Higher-level function for writing solution. Takes care of command line output and calls writecyclefinal to do the rest.
def writesolution(rneig,lneig,mirro,gluetest,label,lvert,vertype,num):
  global solfound;
  global runtotal1,runtotal2;
  print("Solution!");
  solfound += 1;
  print("Number of polygons: " + str(num));
  finn = fname(num);
  fine = finename(lvert,num);
  fullname = filepath+listfile+fine+".txt";
  dex = -1;
  if not fine in runtotal1:
    runtotal1.append(fine);
    runtotal2.append(1);
    dex = len(runtotal1)-1;
    globe = open(fullname,"w");
  else:
    dex = runtotal1.index(fine);
    runtotal2[dex] += 1;
    globe = open(fullname,"a");
  print("Total solutions: "+str(solfound));
  print("Solutions of type "+fine+": "+str(runtotal2[dex]));
  print(verbalvertices(vertype));
  re = vertypesolvedadd(vertype);
  ret = str(vertypesolvedcount[re]);
  versig = signature(vertype);
  print(versig);
  print(writeconway(mirro,gluetest,label)+"\n");
  globe.write("Number of polygons: " + str(num)+"\n");
  globe.write(verbalvertices(vertype)+"\n");
  globe.write(signature(vertype)+"\n");
  filesig = filesignature(vertype);
  checkdirectory(finn,fine,filesig);
  dirsig = finn + "\\" + fine+"\\"+filesig+"\\";
  tesfile1 = dirsig+"eu raw "+filesig+" "+ret+".tes";
  tesfile = filepath+tesfile1;
  solstring = versig+", solution "+ret
  globe.write("TES file: " + tesfile1 + "\n");
  globe.write(writeconway(mirro,gluetest,label)+"\n");
  writecyclefinal(rneig,lneig,lvert,mirro,gluetest,label,globe,tesfile,solstring);
  globe.write("\n");
  globe.close();

# One of the most important parts. This function extends a partial solution by identifying a free edge and trying all possible ways it could be joined, including adding a new vertex and joining the edge to it.
# An added vertex cannot precede the first vertex of the partial solution; this eliminates some possibilities of duplicates.
def extend(n):
  rneig = rneiglist[n];
  lneig = lneiglist[n];
  lvert = lvertlist[n];
  mirro = mirrolist[n];
  glue = gluelist[n];
  num = numlist[n];
  label = labellist[n];
  vertype = vertypelist[n];
  potential = [];
  success = 0;
  gen.write("Extending " + str(n) + ":\n");
  gen.write(verbalvertices(vertype)+"\n");
  gen.write(signature(vertype)+"\n");
  gen.write(str(num)+"\n");
  gen.write(writeconway(mirro,glue,label)+"\n");
  writecycle(rneig,lneig,lvert,glue,label,gen);
  firstfree = mincycle[0];
  if firstfree == -1:
    print(verbalvertices(vertype));
    print(rneig,lneig,lvert,mirro,glue);
  if label[firstfree][0] == "*":
    firstfree = mirro[firstfree];
  if mirro[firstfree] == firstfree:
    mirrored = True;
  else:
    mirrored = False;
  gen.write("firstfree = " + str(firstfree) + "(" + label[firstfree] + ")" + ", between " + str(lvert[firstfree]) + " and " + str(lvert[mirro[firstfree]]) + ". Difference = " + str(mincycle[1]) + "\n");
  for i in range(len(rneig)):
    if glue[i] == -1:
      if mirro[i] == i:
        mirroredi = True;
      else:
        mirroredi = False;
      if mirrored == mirroredi:
        gluetest = glue.copy();
        gluetest[firstfree] = i;
        gluetest[i] = firstfree;
        if not mirrored:
          gluetest[mirro[firstfree]] = mirro[i];
          gluetest[mirro[i]] = mirro[firstfree];
        if checkpart(rneig,lneig,lvert,mirro,gluetest):
          if gluetest.count(-1)==0:
            writesolution(rneig,lneig,mirro,gluetest,label,lvert,vertype,num);
          else:
            success += 1;
            rneiglist.append(rneig);
            lneiglist.append(lneig);
            lvertlist.append(lvert);
            mirrolist.append(mirro);
            gluelist.append(gluetest);
            numlist.append(num);
            labellist.append(label);
            vertypelist.append(vertype);
            potential.append(conwaysymbol(label[firstfree],label[i]));
  if num < maxnum:
    for gr in range(vertype[0],len(symbollist)):
      l = len(rneig);
      rneigtest = rneig.copy();
      lneigtest = lneig.copy();
      lverttest = lvert.copy();
      mirrotest = mirro.copy();
      labeltest = label.copy();
      vertypetest = vertype.copy();
      symbollength = len(rneiglistin[gr])
      for gg in range(symbollength):
        rneigtest.append(l+rneiglistin[gr][gg]);
        lneigtest.append(l+lneiglistin[gr][gg]);
        mirrotest.append(l+mirrolistin[gr][gg]);
        lverttest.append(lvertlistin[gr][gg]);
        labeltest.append(edgelabel(labellistin[gr][gg],num));
      vertypetest.append(gr);
      where = ferk(gr);
      for i in range(l,l+where):
        if mirrotest[i] == i:
          mirroredi = True;
        else:
          mirroredi = False;
        if mirrored == mirroredi:
          gluetest = glue.copy();
          for kse in range(symbollength):
            gluetest.append(-1);
          gluetest[firstfree] = i;
          gluetest[i] = firstfree;
          if not mirrored:
            gluetest[mirrotest[firstfree]] = mirrotest[i];
            gluetest[mirrotest[i]] = mirrotest[firstfree];
          if checkpart(rneigtest,lneigtest,lverttest,mirrotest,gluetest):
            if gluetest.count(-1)==0:
              writesolution(rneigtest,lneigtest,mirrotest,gluetest,labeltest,lverttest,vertypetest,num+1);
            else:
              success += 1;
              rneiglist.append(rneigtest);
              lneiglist.append(lneigtest);
              lvertlist.append(lverttest);
              mirrolist.append(mirrotest);
              gluelist.append(gluetest);
              labellist.append(labeltest);
              numlist.append(num+1);
              vertypelist.append(vertypetest);
              potential.append(conwaysymbol(labeltest[firstfree],labeltest[i])+" "+symbollist[gr]);
  gen.write("Added " + str(success) + " partial solution");
  if success != 1:
    gen.write("s");
  gen.write(", solutions to check: " + str(len(rneiglist)) + "\n");
  if len(potential) > 0:
    for p in range(len(potential)-1):
      gen.write(potential[p]+"; ");
    gen.write(potential[len(potential)-1]+"\n");
  gen.write("\n");
  print(str(str(solcount + 1) + " - " + str(len(rneiglist)))+"         ",end="\r");

# An auxiliary function that sums numbers in a list.
def versum(solved,num):
  sum = 0;
  for i in solved[num]:
    sum += i;
  return sum;

# A function to find the next entry in vertypesolved to be outputed. It's not efficient, but this is an operation that is done only at the very end of the script and it should be negligible compared to the total run time.
def findminimum(solved):
  min = 0;
  minsum = versum(solved,0);
  ind = 1;
  while ind < len(solved):
    indsum = versum(solved,ind);
    if indsum < minsum:
      min = ind;
      minsum = indsum;
    elif indsum == minsum:
      ind2 = 0;
      finished = False;
      while (ind2 < len(solved[ind])) and not finished:
        if solved[ind][ind2] > solved[min][ind2]:
          min = ind;
          finished = True;
        elif solved[ind][ind2] < solved[min][ind2]:
          finished = True;
        ind2 += 1;
    ind += 1;
  return min;

filecount = 1;
initex();
symbolcount = len(symbollist);
gen = open(filepath + genfile + str(filecount) + ".txt","w");
x = len(rneiglist);
while (x > 0):
  y = 0;
  extend(y);
  solcount += 1;
  if solcount % 100000 == 0:
##    filecount += 1;
    gen.close();
    gen = open(filepath + genfile + str(filecount) + ".txt","w");
  del(rneiglist[y]);
  del(lneiglist[y]);
  del(lvertlist[y]);
  del(mirrolist[y]);
  del(gluelist[y]);
  del(labellist[y]);
  del(numlist[y]);
  del(vertypelist[y]);
  x = len(rneiglist);
gen.close();
gen = open(filepath + "eu_final_results.txt","w");
for i in range(len(runtotal1)):
  gen.write(runtotal1[i] + ": " + str(runtotal2[i]) + "\n")
gen.write("\n");
for i in range(len(vertypesolved)):
  while len(vertypesolved) > 0:
    varb = findminimum(vertypesolved);
    print(sig(vertypesolved[varb]));
    gen.write(sig(vertypesolved[varb])+": " + str(vertypesolvedcount[varb]) + "\n");
    del(vertypesolved[varb]);
    del(vertypesolvedcount[varb]);
gen.close();
