#include "testlib.h"

#include<bits/stdc++.h>
#define FOR(i, a, b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, b, a) for (int i = (b), _a = (a); i >= _a; i--)
#define REP(i, n) for (int i = 0, _n = (n); i < _n; i++)
#define FORE(i, v) for (__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define ALL(v) (v).begin(), (v).end()
#define IS_INF(x)   (std::isinf(x))
#define IS_NAN(x)   (std::isnan(x))
#define fi   first
#define se   second
#define MASK(i) (1LL << (i))
#define BIT(x, i) (((x) >> (i)) & 1)
#define div   ___div
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X, class Y>
    bool minimize(X &x, const Y &y) {
        if (x > y) {
            x = y;
            return true;
        } else return false;
    }
template<class X, class Y>
    bool maximize(X &x, const Y &y) {
        if (x < y) {
            x = y;
            return true;
        } else return false;
    }
template<class T>
    T Abs(const T &x) {
        return (x < 0 ? -x : x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE. DRINK A CUP OF TIGERSUGAR BEFORE READING MY CODE. **/

/**
 * Things to check:
 * - Sum of group's sizes does not exceed 10 * numPair.
 * - Each group's elements are distinct.
 * - If i and j are in the same group, they must be friend.
 * - If i and j are friend, they must share some same group.
**/

#define MAX   1111
typedef bitset<MAX> Bitset;

Bitset isFriend[MAX];
int numPerson, numPair;

Bitset marked[MAX], hasCommonGroup[MAX];

void init(void) {
    numPerson = inf.readInt();
    numPair = inf.readInt();
    REP(love, numPair) {
        int u = inf.readInt();
        int v = inf.readInt();
        isFriend[u][v] = true;
        isFriend[v][u] = true;
    }
    FOR(i, 1, numPerson) isFriend[i][i] = true;
}

int checkAnswer(InStream &stream) {
    FOR(i, 1, numPerson) marked[i].reset();
    FOR(i, 1, numPerson) hasCommonGroup[i].reset();

    int numGroup = stream.readInt(0, INT_MAX, "number of groups");

    int sumGroup = 0, sumLimit = 10 * numPair;

    FOR(groupID, 1, numGroup) {
        int groupSize = stream.readInt(0, numPerson, format("groups[%d].size", groupID));
        vector<int> people = stream.readInts(groupSize, 1, numPerson, format("groups[%d]", groupID), 1);

        // - Sum of group's sizes does not exceed 10 * numPair.
        sumGroup += groupSize;
        stream.ensuref(sumGroup <= sumLimit, "Total number of people in all groups exceeds %d.", sumLimit);

        // - Each group's elements are distinct.
        Bitset inGroup;
        FORE(it, people) {
            stream.ensuref(!inGroup[*it], "Person %d appears twice in group %d", *it, groupID);
            inGroup[*it] = true;
        }

        // - If i and j are in the same group, they must be friend.
        REP(i, groupSize) {
            int cur = people[i];
            hasCommonGroup[cur] |= inGroup;
            if ((inGroup & ~isFriend[cur]).none()) continue;

            FORE(jt, people) stream.ensuref(isFriend[cur][*jt], "%d and %d are not friend, but they are both in group %d", cur, *jt, groupID);
            stream.quitf(_fail, "This should not be here :(");
        }
    }

    // - If i and j are friend, they must share some common group.
    FOR(i, 1, numPerson) FOR(j, i + 1, numPerson) if (isFriend[i][j])
        stream.ensuref(hasCommonGroup[i][j], "%d and %d are friend, but they do not share any common group.", i, j);

    return numGroup;
}

double score(int jury, int cont) {
    return cont <= jury ? 1.0 : pow(1.0 * jury / cont, 3);
}

int main(int argc, char* argv[]) {
    registerTestlibCmd(argc, argv);

    init();

    int cont = checkAnswer(ouf);
    int jury = checkAnswer(ans);

    if (cont <= jury) quitf(_ok, "Perfect solution: jury = %d, contestant = %d", jury, cont);
    else quitp(score(jury, cont), "Valid solution: jury = %d, contestant = %d", jury, cont);

    return 0;
}

/*** BUBBLE TEA IS GREAT. MY CODE IS AMAZING :D ***/