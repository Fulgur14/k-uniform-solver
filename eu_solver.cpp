/*
 * eu_solver.cpp
 *
 *  Created on: 10. 12. 2021
 *      Author: Marek
 */

#include <vector>
#include <array>
#include <string>
#include <fstream>
#include <algorithm>
#include <iostream>

std::string solvercode = "eu";
std::string filepath = "solver_" + solvercode + "/";
std::string listfile = solvercode + "solver_";
std::string genfile = solvercode + "output";

constexpr int maxnum = 14;
constexpr int seen = 13;
constexpr int maxpoly = 12;

struct vertexdef {
    std::string symbol;
    std::vector<std::string> label;
    std::vector<int> lneig;
    std::vector<int> rneig;
    std::vector<int> mirro;
    std::vector<int> lvert;
    int ferkval;
    std::string code;
};

struct configuration {
    std::vector<std::string> label;
    std::vector<int> lneig;
    std::vector<int> rneig;
    std::vector<int> mirro;
    std::vector<int> lvert;
    std::vector<int> glue;
    std::vector<int> vertype;
    int num;
    int dfs_depth;
};

std::vector<vertexdef> mainlist = {
        vertexdef{"(3,12,12)A",{"0","1","*0"},{2,0,1},{1,2,0},{2,1,0},{3,12,12},1,"3a"},
        vertexdef{"(3,12,12)F",{"0","1","2","*0","*1","*2"},{2,0,1,4,5,3},{1,2,0,5,3,4},{3,4,5,0,1,2},{3,12,12,12,12,3},2,"3b"},
        vertexdef{"(4,6,12)",{"0","1","2","*0","*1","*2"},{2,0,1,4,5,3},{1,2,0,5,3,4},{3,4,5,0,1,2},{4,12,6,12,6,4},1,"3c"},
        vertexdef{"(6,6,6)S",{"0"},{0},{0},{0},{6},1,"3d"},
        vertexdef{"(6,6,6)R",{"0","*0"},{0,1},{0,1},{1,0},{6,6},2,"3e"},
        vertexdef{"(6,6,6)A",{"0","1","*1"},{2,0,1},{1,2,0},{0,2,1},{6,6,6},1,"3f"},
        vertexdef{"(6,6,6)F",{"0","1","2","*0","*1","*2"},{2,0,1,4,5,3},{1,2,0,5,3,4},{3,4,5,0,1,2},{6,6,6,6,6,6},6,"3g"},
        vertexdef{"(3,3,4,12)",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{3,12,4,3,12,4,3,3},1,"4a"},
        vertexdef{"(3,4,3,12)A",{"0","*0","2","*2"},{3,0,1,2},{1,2,3,0},{1,0,3,2},{3,12,3,4},1,"4b"},
        vertexdef{"(3,4,3,12)F",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{3,12,3,4,12,3,4,3},2,"4c"},
        vertexdef{"(3,3,6,6)A",{"0","1","*0","3"},{3,0,1,2},{1,2,3,0},{2,1,0,3},{3,6,6,3},1,"4d"},
        vertexdef{"(3,3,6,6)F",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{3,6,6,3,6,6,3,3},2,"4e"},
        vertexdef{"(3,6,3,6)S",{"0","*0"},{1,0},{1,0},{1,0},{3,6},1,"4f"},
        vertexdef{"(3,6,3,6)R",{"0","1","*0","*1"},{1,0,3,2},{1,0,3,2},{2,3,0,1},{3,6,6,3},2,"4g"},
        vertexdef{"(3,6,3,6)A1",{"0","1","*1","*0"},{3,0,1,2},{1,2,3,0},{3,2,1,0},{3,6,3,6},2,"4h"},
        vertexdef{"(3,6,3,6)A2",{"0","*0","2","*2"},{3,0,1,2},{1,2,3,0},{1,0,3,2},{3,6,3,6},2,"4i"},
        vertexdef{"(3,6,3,6)F",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{3,6,3,6,6,3,6,3},4,"4j"},
        vertexdef{"(3,4,4,6)",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{3,6,4,4,6,4,4,3},1,"4k"},
        vertexdef{"(3,4,6,4)A",{"0","*0","2","*2"},{3,0,1,2},{1,2,3,0},{1,0,3,2},{4,6,4,3},1,"4l"},
        vertexdef{"(3,4,6,4)F",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{4,6,4,3,6,4,3,4},2,"4m"},
        vertexdef{"(4,4,4,4)S4",{"0"},{0},{0},{0},{4},1,"4n"},
        vertexdef{"(4,4,4,4)R4",{"0","*0"},{0,1},{0,1},{1,0},{4,4},2,"4o"},
        vertexdef{"(4,4,4,4)S2a",{"0","1"},{1,0},{1,0},{0,1},{4,4},2,"4p"},
        vertexdef{"(4,4,4,4)S2b",{"0","*0"},{1,0},{1,0},{1,0},{4,4},2,"4q"},
        vertexdef{"(4,4,4,4)R2",{"0","1","*0","*1"},{1,0,3,2},{1,0,3,2},{2,3,0,1},{4,4,4,4},4,"4r"},
        vertexdef{"(4,4,4,4)A1",{"0","1","2","*1"},{3,0,1,2},{1,2,3,0},{0,3,2,1},{4,4,4,4},2,"4s"},
        vertexdef{"(4,4,4,4)A2",{"0","*0","2","*2"},{3,0,1,2},{1,2,3,0},{1,0,3,2},{4,4,4,4},2,"4t"},
        vertexdef{"(4,4,4,4)F",{"0","1","2","3","*0","*1","*2","*3"},{3,0,1,2,5,6,7,4},{1,2,3,0,7,4,5,6},{4,5,6,7,0,1,2,3},{4,4,4,4,4,4,4,4},8,"4u"},
        vertexdef{"(3,3,3,3,6)A",{"0","*0","2","3","*2"},{4,0,1,2,3},{1,2,3,4,0},{1,0,4,3,2},{3,6,3,3,3},1,"5a"},
        vertexdef{"(3,3,3,3,6)F",{"0","1","2","3","4","*0","*1","*2","*3","*4"},{4,0,1,2,3,6,7,8,9,5},{1,2,3,4,0,9,5,6,7,8},{5,6,7,8,9,0,1,2,3,4},{3,6,3,3,3,6,3,3,3,3},2,"5b"},
        vertexdef{"(3,3,3,4,4)A",{"0","1","*0","3","*3"},{4,0,1,2,3},{1,2,3,4,0},{2,1,0,4,3},{3,4,4,3,3},1,"5c"},
        vertexdef{"(3,3,3,4,4)F",{"0","1","2","3","4","*0","*1","*2","*3","*4"},{4,0,1,2,3,6,7,8,9,5},{1,2,3,4,0,9,5,6,7,8},{5,6,7,8,9,0,1,2,3,4},{3,4,4,3,3,4,4,3,3,3},2,"5d"},
        vertexdef{"(3,3,4,3,4)A",{"0","1","*1","*0","4"},{4,0,1,2,3},{1,2,3,4,0},{3,2,1,0,4},{3,4,3,4,3},1,"5e"},
        vertexdef{"(3,3,4,3,4)F",{"0","1","2","3","4","*0","*1","*2","*3","*4"},{4,0,1,2,3,6,7,8,9,5},{1,2,3,4,0,9,5,6,7,8},{5,6,7,8,9,0,1,2,3,4},{3,4,3,4,3,4,3,4,3,3},2,"5f"},
        vertexdef{"(3,3,3,3,3,3)S6",{"0"},{0},{0},{0},{3},1,"6a"},
        vertexdef{"(3,3,3,3,3,3)R6",{"0","*0"},{0,1},{0,1},{1,0},{3,3},2,"6b"},
        vertexdef{"(3,3,3,3,3,3)S3a",{"0","1"},{1,0},{1,0},{0,1},{3,3},2,"6c"},
        vertexdef{"(3,3,3,3,3,3)S3b",{"0","*0"},{1,0},{1,0},{1,0},{3,3},2,"6d"},
        vertexdef{"(3,3,3,3,3,3)R3",{"0","1","*0","*1"},{1,0,3,2},{1,0,3,2},{2,3,0,1},{3,3,3,3},4,"6e"},
        vertexdef{"(3,3,3,3,3,3)S2",{"0","1","*1"},{2,0,1},{1,2,0},{0,2,1},{3,3,3},1,"6f"},
        vertexdef{"(3,3,3,3,3,3)R2",{"0","1","2","*0","*1","*2"},{2,0,1,4,5,3},{1,2,0,5,3,4},{3,4,5,0,1,2},{3,3,3,3,3,3},6,"6g"},
        vertexdef{"(3,3,3,3,3,3)A1",{"0","1","2","3","*2","*1"},{5,0,1,2,3,4},{1,2,3,4,5,0},{0,5,4,3,2,1},{3,3,3,3,3,3},2,"6h"},
        vertexdef{"(3,3,3,3,3,3)A2",{"0","1","2","*2","*1","*0"},{5,0,1,2,3,4},{1,2,3,4,5,0},{5,4,3,2,1,0},{3,3,3,3,3,3},2,"6i"},
        vertexdef{"(3,3,3,3,3,3)F",{"0","1","2","3","4","5","*0","*1","*2","*3","*4","*5"},{5,0,1,2,3,4,7,8,9,10,11,6},{1,2,3,4,5,0,11,6,7,8,9,10},{6,7,8,9,10,11,0,1,2,3,4,5},{3,3,3,3,3,3,3,3,3,3,3,3},12,"6j"}
};

int symbolcount;

struct runt {
    std::string soltype;
    int solnum;
};

std::vector<runt> runtotal;

struct vertypesolv {
    std::vector<int> vertices;
    int count;
};

std::vector<vertypesolv> vertypesolved;

int solcount = 0;
int solfound = 0;

std::vector<int> mincycle;

std::ofstream globe;
std::ofstream gen;

std::string fname(int num);
std::string finename(configuration const& conf);
int ferk(vertexdef const& x);
std::string edgelabel(std::string edge, int tile);
std::string conwaysymbol(std::string const& first, std::string const& second);
std::string writeconway(configuration const& conf);
std::string verbalvertices(std::vector<int> const& vertype);
bool checkpart(configuration const& conf);
int writecycle(configuration const& conf, std::ostream& filen);
std::vector<int> sigresult(std::vector<int> const& vertype);
std::string sig(std::vector<int> const& result);
std::string signature(std::vector<int> const& vertype);
std::string filesignature(std::vector<int> const& vertype);
int vertypesolvedadd(std::vector<int> const& vertype);
int initex();
int writecyclefinal(configuration const& conf, std::ostream& filen);
int writesolution(configuration const& conf);

bool simplify(configuration const& conf);
int extend(configuration& slist);

std::string finename(configuration const& conf) {
    std::string m = fname(conf.num) + "_";
    if (std::find(conf.lvert.begin(), conf.lvert.end(), 3) != conf.lvert.end()) {
        m = m + "3";
    }
    if (std::find(conf.lvert.begin(), conf.lvert.end(), 4) != conf.lvert.end()) {
        m = m + "4";
    }
    if (std::find(conf.lvert.begin(), conf.lvert.end(), 6) != conf.lvert.end()) {
        m = m + "6";
    }
    if (std::find(conf.lvert.begin(), conf.lvert.end(), 12) != conf.lvert.end()) {
        m = m + "c";
    }
    return m;
}

std::string fname(int num) {
    std::string m = std::to_string(num);
    if (num < 10) {
        m = "0" + m;
    }
    return m;
}

int ferk(vertexdef const& x) {
    int r = x.lneig.size();
    int q = r / x.ferkval;
    return q;
}

std::string edgelabel(std::string edge, int tile) {
    std::string m = edge;
    if (tile > 3) {
        m = m + "@" + std::to_string(tile);
    }
    else {
        for (int i = 0; i < tile; i++) {
            m = m + "'";
        }
    }
    return m;
}

std::string conwaysymbol(std::string const& first, std::string const& second) {
    int mirrornum = 0;
    std::string mfirst = first;
    std::string msecond = second;
    if (first[0] == '*') {
        mfirst = mfirst.substr(1);
        mirrornum++;
    }
    if (second[0] == '*') {
        msecond = msecond.substr(1);
        mirrornum++;
    }
    bool same = mfirst == msecond;
    if (mirrornum != 1) {
        if (same) {
            return "(" + mfirst + ")";
        }
        else {
            return "(" + mfirst + " " + msecond + ")";
        }
    }
    else {
        if (same) {
            return "[" + mfirst + "]";
        }
        else {
            return "[" + mfirst + " " + msecond + "]";
        }
    }
}

std::string writeconway(configuration const& conf) {
    std::vector<int> smet = {};
    std::string conwaystring = "";
    for (int cy = 0; cy < (int)conf.glue.size(); cy++) {
        if ((std::find(smet.begin(), smet.end(), cy) == smet.end()) && (conf.glue[cy] != -1)) {
            std::string first = conf.label[cy];
            std::string second = conf.label[conf.glue[cy]];
            smet.push_back(cy);
            smet.push_back(conf.glue[cy]);
            smet.push_back(conf.mirro[cy]);
            smet.push_back(conf.glue[conf.mirro[cy]]);
            conwaystring = conwaystring + conwaysymbol(first, second);
        }
    }
    return conwaystring;
}

std::string verbalvertices(std::vector<int> const& vertype) {
    std::string s = "";
    for (int i : vertype) s = s + mainlist[i].symbol + ", ";
    return s.substr(0, s.size() - 2);
}

bool checkpart(configuration const& conf) {
    for (int i = 0; i < (int)conf.rneig.size(); i++) {
        int free = i;
        int rfree = conf.rneig[free];
        int vfree = conf.lvert[rfree];
        int mainvert = vfree;
        int count = 1;
        bool passt = false;
        while (!passt) {
            free = conf.glue[rfree];
            if (free == -1) {
                if (count > mainvert) {
                    return false;
                }
                else {
                    passt = true;
                }
            }
            else if (free == i) {
                if (mainvert % count != 0) {
                    return false;
                }
                else {
                    passt = true;
                }
            }
            else {
                rfree = conf.rneig[free];
                vfree = conf.lvert[rfree];
                count++;
                if (vfree != mainvert) {
                    return false;
                }
            }
        }
    }
    return true;
}

int writecycle(configuration const& conf, std::ostream& filen) {
    mincycle = { -1,maxpoly + 1 };
    int v = 0;
    std::vector<int> smet = {};
    for (int cy = 0; cy < (int)conf.glue.size(); cy++) {
        std::string mainst = "";
        int count = 0;
        bool complete = false;
        if (std::find(smet.begin(), smet.end(), cy) == smet.end()) {
            int left = cy;
            while ((conf.glue[left] != -1) && (conf.glue[left] != conf.rneig[cy])) {
                left = conf.lneig[conf.glue[left]];
            }
            if (conf.glue[left] == -1) {
                int stable = left;
                int right = conf.rneig[left];
                int vstable = conf.lvert[right];
                bool cont = true;
                while (cont) {
                    smet.push_back(left);
                    mainst = mainst + conf.label[left] + "/" + conf.label[right] + "(" + std::to_string(conf.lvert[right]) + ")-";
                    count++;
                    left = conf.glue[right];
                    if (left != -1) {
                        right = conf.rneig[left];
                    }
                    else {
                        int dif = vstable - count;
                        if (dif < mincycle[1]) {
                            mincycle = { stable,dif };
                        }
                        cont = false;
                    }
                }
            }
            else {
                left = cy;
                int right = conf.rneig[left];
                v = conf.lvert[right];
                bool cont = true;
                complete = true;
                while (cont) {
                    smet.push_back(left);
                    mainst = mainst + conf.label[left] + "/" + conf.label[right] + "(" + std::to_string(conf.lvert[right]) + ")-";
                    count++;
                    left = conf.glue[right];
                    if (left != cy) {
                        right = conf.rneig[left];
                    }
                    else {
                        cont = false;
                    }
                }
            }
            if (complete) {
                mainst = mainst.substr(0, mainst.size() - 1);
                int ratio = v / count;
                if (ratio != 1) {
                    mainst = " [" + mainst + "]x" + std::to_string(ratio);
                }
                else {
                    mainst = " " + mainst;
                }
            }
            filen << mainst << "\n";
        }
    }
    return 0;
}

std::string sig(std::vector<int> const& result) {
    std::string s = "";
    for (int i = 0; i < (int)result.size(); i++) {
        if (result[i] > 0) {
            s = s + mainlist[i].symbol;
            if (result[i] > 1) {
                s = s + "x" + std::to_string(result[i]);
            }
            s = s + ", ";
        }
    }
    return s.substr(0, s.size() - 2);
}

std::vector<int> sigresult(std::vector<int> const& vertype) {
    std::vector<int> result(symbolcount, 0);
    for (int i : vertype) result[i]++;
    return result;
}

std::string signature(std::vector<int> const& vertype) {
    return sig(sigresult(vertype));
}

std::string filesignature(std::vector<int> const& vertype) {
    std::vector<int> result = sigresult(vertype);
    std::string s = "";
    for (int i = 0; i < (int)result.size(); i++) {
        if (result[i] > 0) {
            s = s + mainlist[i].code;
            if (result[i] > 1) {
                s = s + std::to_string(result[i]);
            }
            s = s + " ";
        }
    }
    return s.substr(0, s.size() - 1);
}

int vertypesolvedadd(std::vector<int> const& vertype) {
    std::vector<int> result = sigresult(vertype);
    std::vector<int> res2;
    int x = 0;
    while (x < (int)vertypesolved.size()) {
        res2 = vertypesolved[x].vertices;
        if (result == res2) {
            vertypesolved[x].count++;
            return x;
        }
        x++;
    }
    vertypesolved.push_back({ result,1 });
    return x;
}

int initex() {
    for (int i = 0; i < symbolcount; i++) {
        configuration newconf;
        newconf.label = mainlist[i].label;
        newconf.lneig = mainlist[i].lneig;
        newconf.rneig = mainlist[i].rneig;
        newconf.mirro = mainlist[i].mirro;
        newconf.lvert = mainlist[i].lvert;
        newconf.vertype = { i };
        newconf.num = 1;
        newconf.dfs_depth = 0;
        newconf.glue = std::vector<int>(newconf.lneig.size(), -1);
        extend(newconf);
    }
    return 0;
}


int writecyclefinal(configuration const& conf, std::ostream& filen) {
    int v = 0;
    std::vector<int> smet = {};
    std::vector<std::string> mainstlist = {};
    std::vector<int> sublist = {};
    bool ultrachiral = true;
    std::vector<int> repeatlist = {};
    for (int cy = 0; cy < (int)conf.glue.size(); cy++) {
        std::string mainst = "";
        int count = 0;
        int minmirror = conf.glue.size();
        if (std::find(smet.begin(), smet.end(), cy) == smet.end()) {
            int left = cy;
            int right = conf.rneig[left];
            v = conf.lvert[right];
            bool cont = true;
            while (cont) {
                smet.push_back(left);
                if (conf.mirro[right] < minmirror) {
                    minmirror = conf.mirro[right];
                }
                mainst = mainst + conf.label[left] + "/" + conf.label[right] + "(" + std::to_string(conf.lvert[right]) + ")-";
                count++;
                left = conf.glue[right];
                if (left != cy) {
                    right = conf.rneig[left];
                }
                else {
                    cont = false;
                }
            }
            mainst = mainst.substr(0, mainst.size() - 1);
            int ratio = v / count;
            repeatlist.push_back(ratio);
            if (ratio != 1) {
                mainst = "[" + mainst + "]x" + std::to_string(ratio);
            }
            mainstlist.push_back(mainst);
            if (std::find(smet.begin(), smet.end(), minmirror) != smet.end()) {
                sublist.push_back(0);
                ultrachiral = false;
            }
            else {
                int left = minmirror;
                mainst = "";
                right = conf.rneig[left];
                v = conf.lvert[right];
                cont = true;
                while (cont) {
                    smet.push_back(left);
                    mainst = mainst + conf.label[left] + "/" + conf.label[right] + "(" + std::to_string(conf.lvert[right]) + ")-";
                    count++;
                    left = conf.glue[right];
                    if (left != minmirror) {
                        right = conf.rneig[left];
                    }
                    else {
                        cont = false;
                    }
                }
                mainst = mainst.substr(0, mainst.size() - 1);
                repeatlist.push_back(ratio);
                if (ratio != 1) {
                    mainst = "[" + mainst + "]x" + std::to_string(ratio);
                }
                mainstlist.push_back(mainst);
                sublist.push_back(1);
                sublist.push_back(2);
            }
        }
    }
    std::string header;
    std::string subheader;
    for (int m = 0; m < (int)mainstlist.size(); m++) {
        std::string mainst = mainstlist[m];
        int sub = sublist[m];
        if (sub == 0) {
            filen << std::to_string(m) << ": " << mainst;
        }
        else if (sub == 1) {
            if (!ultrachiral) {
                header = std::to_string(m) + "/" + std::to_string(m + 1) + ": ";
            }
            else {
                header = std::to_string(m / 2) + ": ";
            }
            subheader = std::string(header.size(), ' ');
            filen << header << mainst;
        }
        else {
            filen << subheader << mainst;
        }
        filen << "\n";
    }
    filen << "---\n";
    return 0;
}

int writesolution(configuration const& conf) {
    std::cout << "\nSolution!\n";
    solfound++;
    std::cout << "Number of vertices: " << std::to_string(conf.num) << "\n";
    std::string finn = fname(conf.num);
    std::string fine = finename(conf);
    std::string fullname = filepath + listfile + fine + "_" + std::to_string(conf.dfs_depth) + ".txt";
    int dex = -1;
    int x = 0;
    bool found = false;
    while ((x < (int)runtotal.size()) && !found) {
        if (fine == runtotal[x].soltype) {
            runtotal[x].solnum++;
            dex = x;
            found = true;
            globe.open(fullname, std::ios::app);
        }
        x++;
    }
    if (!found) {
        runtotal.push_back(runt{ fine,1 });
        dex = runtotal.size() - 1;
        globe.open(fullname);
    }
    std::cout << "Total solutions: " << std::to_string(solfound) << "\n";
    std::cout << "Solutions of type " << fine << ": " << std::to_string(runtotal[dex].solnum) << "\n";
    std::string vv = verbalvertices(conf.vertype);
    std::cout << vv << "\n";
    int re = vertypesolvedadd(conf.vertype);
    std::string ret = std::to_string(vertypesolved[re].count);
    std::string versig = signature(conf.vertype);
    std::cout << versig << "\n";
    std::string wc = writeconway(conf);
    std::cout << wc << "\n";
    globe << "Number of vertex types: " << std::to_string(conf.num) << "\n";
    // globe << "DFS depth: " << conf.dfs_depth << "\n";
    globe << vv << "\n";
    globe << versig << "\n";
    std::string filesig = filesignature(conf.vertype);
    std::string tesfile1 = solvercode + " raw " + filesig + " " + ret + ".tes";
    globe << "TES file: " << tesfile1 << "\n";
    globe << wc << "\n";
    writecyclefinal(conf, globe);
    globe << "\n";
    globe.close();
    return 0;
}

bool simplify(configuration const& conf) {
    int le = conf.rneig.size();

    std::vector<int> eq_class(le, 0);

    int num_eq_class = 1;

    int last_num_eq_class = 0;

    while (num_eq_class > last_num_eq_class) {
        using vertex_data = std::array<int, 6>;
        std::vector<std::pair<vertex_data, int > > data(le);

        last_num_eq_class = num_eq_class;
        for (int i = 0; i < le; i++) {
            data[i].first[0] = conf.lvert[i];
            data[i].first[1] = eq_class[i];
            data[i].first[2] = eq_class[conf.mirro[i]];
            data[i].first[3] = eq_class[conf.glue[i]];
            data[i].first[4] = eq_class[conf.lneig[i]];
            data[i].first[5] = eq_class[conf.rneig[i]];
            data[i].second = i;
        }

        sort(data.begin(), data.end());
        eq_class[data[0].second] = 0;

        num_eq_class = 0;

        for (int i = 1; i < le; i++) {
            if (data[i].first != data[i - 1].first) num_eq_class++;
            eq_class[data[i].second] = num_eq_class;
        }

        num_eq_class++;
    }

    return num_eq_class == le;
}

int extend(configuration& slist) {
    slist.dfs_depth++;
    std::vector<std::string> potential = {};
    int success = 0;
    if (solcount % 100000 == 0) {
        gen.close();
        gen.open(filepath + genfile + "1.txt");
    }
    gen << "Resolving configuration " << solcount + 1 << "\n";
    gen << verbalvertices(slist.vertype) << "\n";
    gen << signature(slist.vertype) << "\n";
    gen << std::to_string(slist.num) << "\n";
    gen << writeconway(slist) << "\n";
    writecycle(slist, gen);
    int firstfree;
    int minc;
    firstfree = mincycle[0];
    minc = mincycle[1];
    if (slist.label[firstfree][0] == '*') {
        firstfree = slist.mirro[firstfree];
    }
    bool mirrored = (slist.mirro[firstfree] == firstfree);
    gen << "firstfree = " << std::to_string(firstfree) << "(" << slist.label[firstfree] << "), between " <<
        std::to_string(slist.lvert[firstfree]) << " and " << std::to_string(slist.lvert[slist.mirro[firstfree]]) <<
        ". Difference = " << std::to_string(minc) << "\n";
    for (int i = 0; i < (int)slist.rneig.size(); i++) {
        if (slist.glue[i] == -1) {
            bool mirroredi = slist.mirro[i] == i;
            if (mirrored == mirroredi) {
                slist.glue[firstfree] = i;
                slist.glue[i] = firstfree;
                if (!mirrored) {
                    slist.glue[slist.mirro[firstfree]] = slist.mirro[i];
                    slist.glue[slist.mirro[i]] = slist.mirro[firstfree];
                }
                configuration& newconf = slist;
                if (checkpart(newconf)) {
                    if (std::find(newconf.glue.begin(), newconf.glue.end(), -1) == newconf.glue.end()) {
                        if (newconf.num > seen) {
                            if (simplify(newconf)) {
                                writesolution(newconf);
                            }
                        }
                    }
                    else {
                        success++;
                        extend(newconf);
                        potential.push_back(conwaysymbol(newconf.label[firstfree], newconf.label[i]));
                    }
                }
                slist.glue[firstfree] = -1;
                slist.glue[i] = -1;
                if (!mirrored) {
                    slist.glue[slist.mirro[firstfree]] = -1;
                    slist.glue[slist.mirro[i]] = -1;
                }
            }
        }
    }
    if (slist.num < maxnum) {
        for (int gr = slist.vertype[0]; gr < symbolcount; gr++) {
            int l = slist.rneig.size();
            configuration& newconf = slist;
            int symbollength = mainlist[gr].rneig.size();
            for (int gg = 0; gg < symbollength; gg++) {
                newconf.rneig.push_back(l + mainlist[gr].rneig[gg]);
                newconf.lneig.push_back(l + mainlist[gr].lneig[gg]);
                newconf.mirro.push_back(l + mainlist[gr].mirro[gg]);
                newconf.lvert.push_back(mainlist[gr].lvert[gg]);
                newconf.label.push_back(edgelabel(mainlist[gr].label[gg], newconf.num));
                newconf.glue.push_back(-1);
            }
            newconf.vertype.push_back(gr);
            newconf.num++;
            int ran = ferk(mainlist[gr]);
            for (int i = l; i < l + ran; i++) {
                configuration& newconf2 = newconf;
                bool mirroredi = newconf2.mirro[i] == i;
                if (mirrored == mirroredi) {
                    newconf2.glue[firstfree] = i;
                    newconf2.glue[i] = firstfree;
                    if (!mirrored) {
                        newconf2.glue[newconf2.mirro[firstfree]] = newconf2.mirro[i];
                        newconf2.glue[newconf2.mirro[i]] = newconf2.mirro[firstfree];
                    }
                    if (checkpart(newconf2)) {
                        if (std::find(newconf2.glue.begin(), newconf2.glue.end(), -1) == newconf2.glue.end()) {
                            if (newconf2.num > seen) {
                                if (simplify(newconf2)) {
                                    writesolution(newconf2);
                                }
                            }
                        }
                        else {
                            success++;
                            extend(newconf2);
                            potential.push_back(conwaysymbol(newconf2.label[firstfree], newconf2.label[i]) + " " + mainlist[gr].symbol);
                        }
                    }
                    newconf2.glue[firstfree] = -1;
                    newconf2.glue[i] = -1;
                    if (!mirrored) {
                        newconf2.glue[newconf2.mirro[firstfree]] = -1;
                        newconf2.glue[newconf2.mirro[i]] = -1;
                    }
                }
            }
            newconf.num--;
            newconf.vertype.pop_back();
            newconf.rneig.resize(l);
            newconf.lneig.resize(l);
            newconf.mirro.resize(l);
            newconf.lvert.resize(l);
            newconf.label.resize(l);
            newconf.glue.resize(l);
        }
    }
    gen << "Added " << std::to_string(success) << " partial solution";
    if (success != 1) {
        gen << "s";
    }
    gen << "\n";
    if (potential.size() > 0) {
        for (int p = 0; p < (int)potential.size() - 1; p++) {
            gen << potential[p] << "; ";
        }
        gen << potential[potential.size() - 1] << "\n";
    }
    gen << "\n";
    solcount++;
    std::cout << std::to_string(solcount) << " - depth " << slist.dfs_depth << "      \r";
    slist.dfs_depth--;
    return 0;
}

int main() {
    symbolcount = mainlist.size();
    int filecount = 1;
    gen.open(filepath + genfile + std::to_string(filecount) + ".txt");
    initex();
    gen.close();
    return 0;
}