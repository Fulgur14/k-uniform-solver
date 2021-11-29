import math;
import os;

# Path for the output directory; must exist before the program is started. You should change it to your desired path.
filepathi = "c:\\_preklad\\_knihy\\hyperrogue\\euclidean\\";
filepath = filepathi+"pruned\\";

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

siglist = [];
sollist = [];

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

# The main output: writes a *.tes file, ready for use in HyperRogue.
def teswrite(conway,polysizelist,repeatlist,tesfi,solstring):
  tesdir = filepath + filecodebase + "\\";
  if not os.path.exists(tesdir):
     os.makedirs(tesdir)
  tesdir = tesdir + countsignature + "\\";
  if not os.path.exists(tesdir):
     os.makedirs(tesdir)
  tesind = tesfi.index("raw");
  tesf = "eu "+tesfi[tesind+4:]
  tesfile = tesdir + tesf;
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

def deciphersymbol(symbol,label):
  if symbol[0] == '[':
    mirror = True;
  else:
    mirror = False;
  first = "";
  ind = 1;
  while not symbol[ind] in [' ',')',']']:
    first = first + symbol[ind];
    ind += 1;
  if symbol[ind] == ' ':
    ind += 1;
    second = "";
    while not symbol[ind] in [')',']']:
      second = second + symbol[ind];
      ind += 1;
  else:
    second = first;
  if mirror:
    second = "*"+second;
  return [first,second];

def isnumeral(ch):
  if ch in ["0","1","2","3","4","5","6","7","8","9"]:
    return True;
  else:
    return False;

def decipher(x):
  i = 0;
  k = "";
  stri = x + " ";
  mirror = False;
  num=0;
  til=0;
  if stri[i] == "*":
    mirror=True;
    i += 1;
  while isnumeral(stri[i]):
    num = num*10 + int(stri[i]);
    i += 1;
  while stri[i] == "'":
    til += 1;
    i += 1;
  if stri[i] == "@":
    i += 1;
    while isnumeral(stri[i]):
      til = til*10 + int(stri[i]);
      i += 1;
  return [mirror,num,til];

def findindex(conway):
  for i in range(len(conway)):
    if conway[i] in [')',']']:
      return i;
  return -1;

def makeglue(c,mirro,label):
  conway = c;
  gluetest = [];
  for i in range(len(mirro)):
    gluetest.append(-1);
  while len(conway) > 1:
    ind = findindex(conway);
    symbol = conway[:ind+1];
    conway = conway[ind+1:];
    t = deciphersymbol(symbol,label);
    k = [];
    for i in range(2):
      st = "";
      w = decipher(t[i]);
      if w[0]:
        st = st + "*";
      st = st + edgelabel(w[1],w[2]);
      k.append(label.index(st));
    gluetest[k[0]] = k[1];
    gluetest[k[1]] = k[0];
    gluetest[mirro[k[0]]] = mirro[k[1]];
    gluetest[mirro[k[1]]] = mirro[k[0]];
  return gluetest;

def codcon(x):
  if codcon == 10:
    return "a";
  elif codcon == 11:
    return "b";
  else:
    return str(x);

def buildvertextypes(vertypeline):
  global countsignature;
  vertextypes = [];
  g = vertypeline[:-1]+", ";
  sym2list = [];
  sym2code = [];
  while len(g) > 0:
    ind = g.index(" ");
    sym = g[:ind-1];
    sym2i = sym.index(")");
    sym2 = sym[0:sym2i+1];
    if not sym2 in sym2list:
      sym2list.append(sym2);
      sym2code.append(1);
      sym2sig = len(sym2list)-1;
    else:
      sym2sig = sym2list.index(sym2);
      sym2code[sym2sig] += 1;
    g = g[ind+1:];
    ind2 = symbollist.index(sym);
    vertextypes.append(ind2);
  countsignature = str(len(sym2list));
  secsig = " (";
  high = False;
  while len(sym2code)>0:
    m = max(sym2code);
    if m > 1:
      high = True;
    ind = sym2code.index(m);
    del(sym2code[ind]);
    secsig = secsig + codcon(m);
  secsig = secsig + ")";
  if high:
    countsignature = countsignature + secsig;
  return vertextypes;

def decode(vertypeline,signatureline,tesline,conwayline):
  global rneig,lneig,mirro,lvert,glue,label;
  rneig = [];
  lneig = [];
  mirro = [];
  lvert = [];
  glue = [];
  label = [];
  vertextypes = buildvertextypes(vertypeline);
  for j in range(len(vertextypes)):
    i = vertextypes[j];
    l = len(rneig);
    symbollength = len(rneiglistin[i])
    for gg in range(symbollength):
      rneig.append(l+rneiglistin[i][gg]);
      lneig.append(l+lneiglistin[i][gg]);
      mirro.append(l+mirrolistin[i][gg]);
      lvert.append(lvertlistin[i][gg]);
      label.append(edgelabel(labellistin[i][gg],j));
  glue = makeglue(conwayline,mirro,label);

def simplify(rneig,lneig,mirro,lvert,glue,label):
  fullset = set();
  alias = [];
  le = len(rneig);
  unique = [];
  for i in range(le):
    fullset.add(i);
    unique.append(False);
  for i in range(le):
    alias.append(fullset.copy());
  change = True;
  while change:
    change = False;
    for i in range(le):
      ali = alias[i].copy();
      for j in ali:
        if lvert[i] != lvert[j]:
#          print(label[i] +"("+str(lvert[i])+") != "+label[j]+"("+str(lvert[j])+")");
          alias[i].remove(j);
          change = True;
        elif not i in alias[j]:
#          print(label[j] + " is in " + label[i] + ", but " + label[i] + " is not in " + label[j]);
          alias[i].remove(j);
          change = True;
        elif not mirro[j] in alias[mirro[i]]:
#          print(label[j] + " is in " + label[i] + ", but mirror " + label[mirro[j]] + " is not in " + label[mirro[i]]);
          alias[i].remove(j);
          change = True;
        elif not glue[j] in alias[glue[i]]:
#          print(label[j] + " is in " + label[i] + ", but connected " + label[glue[j]] + " is not in " + label[glue[i]]);
          alias[i].remove(j);
          change = True;
        elif not rneig[j] in alias[rneig[i]]:
#          print(label[j] + " is in " + label[i] + ", but right " + label[rneig[j]] + " is not in " + label[rneig[i]]);
          alias[i].remove(j);
          change = True;
        elif not lneig[j] in alias[lneig[i]]:
#          print(label[j] + " is in " + label[i] + ", but left " + label[lneig[j]] + " is not in " + label[lneig[i]]);
          alias[i].remove(j);
          change = True;
      if len(alias[i]) == 1:
        unique[i] = True;
  nun = False in unique;
  if nun:
    t = "";
    rlist = set();
    for i in range(len(unique)):
      if (not i in rlist) and len(alias[i]) > 1:
        s = "[";
        for j in alias[i]:
          s = s + label[j] + "/";
          rlist.add(j);
        s = s[:-1]+"] ";
        t = t+s;
    raw.write(t[:-1]+"\n");
  return not nun;

def addsolution(rneig,lneig,lvert,mirro,glue,label,sigline):
  global rneiglist,lneiglist,lvertlist,mirrolist,gluelist,labellist;
  rneiglist.append(rneig);
  lneiglist.append(lneig);
  lvertlist.append(lvert);
  mirrolist.append(mirro);
  gluelist.append(glue);
  labellist.append(label);
  if not sigline in siglist:
    siglist.append(sigline);
    sollist.append([]);
    sigcode = len(siglist)-1;
  else:
    sigcode = siglist.index(sigline);
  sollist[sigcode].append(len(rneiglist)-1);

def comparesolutions(rneigx,lneigx,lvertx,mirrox,gluex,labelx,sol):
  fullset1 = set();
  fullset2 = set();
  alias = [];
  le = len(rneigx);
  unique = [];
  for i in range(le):
    fullset1.add(le+i);
    fullset2.add(i);
    unique.append(False);
  for i in range(le):
    alias.append(fullset1.copy());
    alias[i].add(i);
    unique.append(False);
  rneig = rneigx.copy();
  lneig = lneigx.copy();
  mirro = mirrox.copy();
  glue = gluex.copy();
  label = labelx.copy();
  lvert = lvertx.copy();
  for i in range(le):
    alias.append(fullset2.copy());
    alias[le+i].add(le+i);
    rneig.append(le+rneiglist[sol][i]);
    lneig.append(le+lneiglist[sol][i]);
    mirro.append(le+mirrolist[sol][i]);
    glue.append(le+gluelist[sol][i]);
    lvert.append(lvertlist[sol][i]);
    label.append(labellist[sol][i]);
  change = True;
  while change:
    change = False;
    for i in range(le*2):
      ali = alias[i].copy();
      for j in ali:
        if lvert[i] != lvert[j]:
          alias[i].remove(j);
          change = True;
        elif not i in alias[j]:
          alias[i].remove(j);
          change = True;
        elif not mirro[j] in alias[mirro[i]]:
          alias[i].remove(j);
          change = True;
        elif not glue[j] in alias[glue[i]]:
          alias[i].remove(j);
          change = True;
        elif not rneig[j] in alias[rneig[i]]:
          alias[i].remove(j);
          change = True;
        elif not lneig[j] in alias[lneig[i]]:
          alias[i].remove(j);
          change = True;
      if len(alias[i]) == 1:
        unique[i] = True;
  nun = False in unique;
  if nun:
    t = "";
    rlist = set();
    for i in range(len(unique)):
      if (not i in rlist) and len(alias[i]) > 1:
        s = "[";
        for j in alias[i]:
          s = s + label[j] + "=";
          rlist.add(j);
        s = s[:-1]+"] ";
        t = t+s;
    raw.write(t[:-1]+"\n");
    print(t);
  return nun;

def compare(rneig,lneig,lvert,mirro,glue,label,sigline):
  if not sigline in siglist:
    return False;
  sigcode = siglist.index(sigline);
  i = 0;
  le = len(sollist[sigcode])
  found = False;
  while (i < le) and not found:
    found = comparesolutions(rneig,lneig,lvert,mirro,glue,label,sollist[sigcode][i]);
    i += 1;
  return found;

def processfile(filec):
  global raw, globe;
  filecode = filecodebase + "_"+filec;
  listfile = "eusolver_"+filecode+".txt";
  outputfile = "eupruned_"+filecode+".txt";
  rawfile = "euraw_"+filecode+".txt";
  symbolcount = len(symbollist);
  prunefile = open(filepathi+listfile,"r")
  globe = open(filepath+outputfile,"w");
  raw = open(filepath+rawfile,"w");
  prune = prunefile.readlines();
  prunefile.close();
  lpr = len(prune);
  linecount = 0;
  while (linecount < lpr):
    origlinecount = linecount;
    linecount += 1;
    vertypeline = prune[linecount];
    linecount += 1;
    signatureline = prune[linecount];
    linecount += 1;
    tesline = prune[linecount];
    linecount += 1;
    conwayline = prune[linecount];
    linecount += 1;
    while prune[linecount][0] != "-":
      linecount += 1;
    linecount += 3;
    decode(vertypeline,signatureline,tesline,conwayline);
    print(vertypeline[:-1]);
    print(signatureline[:-1]);
    print(conwayline[:-1]);
    raw.write(vertypeline);
    raw.write(signatureline);
    raw.write(tesline);
    raw.write(conwayline);
    simplest = simplify(rneig,lneig,mirro,lvert,glue,label);
    if simplest:
      print("Simplest");
      raw.write("Simplest\n");
      seen = compare(rneig,lneig,lvert,mirro,glue,label,signatureline[:-1]);
      if not seen:
        addsolution(rneig,lneig,lvert,mirro,glue,label,signatureline[:-1]);
        tescolon = tesline.index("eu");
        tesfile = tesline[tescolon:-1];
        globe.write(vertypeline);
        globe.write(signatureline);
        globe.write("Count type: " + countsignature+"\n");
        globe.write(tesline);
        globe.write(conwayline);
        writecyclefinal(rneig,lneig,lvert,mirro,glue,label,globe,tesfile,signatureline[:-1]);
        globe.write("\n");
    print();
    raw.write("\n");
  globe.close();
  raw.close();

def metaprocess(fcode):
  global filecodebase;
  filecodebase = fcode;
  processfile("34");
  processfile("346");
  processfile("346c");
  processfile("34c");
  processfile("36");

metaprocess("02");
metaprocess("03");
metaprocess("04");
metaprocess("05");
metaprocess("06");
metaprocess("07");
metaprocess("08");
metaprocess("09");
metaprocess("10");
metaprocess("11");
metaprocess("12");
