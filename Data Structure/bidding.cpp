#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    // enter how many bidder
    int howmany;
    cin >> howmany;

    // enter each bidder's name and money
    string name; int money;

    // container of bidders
    map<int, vector<string>, greater<int>> bidders;

    // insert bidder to container
    for(int i = 0; i < howmany; i++) {
        cin >> name >> money;
        auto iter = bidders.find(money);
        // already money exist
        if(iter != bidders.end())
            bidders[money].push_back(name);
        // not yet
        else
            bidders[money] = {name};
    }

    auto i = bidders.begin();

    for(; i != bidders.end(); i++){
        if(i->second.size() == 1) {
            cout << i->second[0] << endl;
            break;
        }
    }

    if(i == bidders.end())
        cout << "NONE";

    return 0;
}