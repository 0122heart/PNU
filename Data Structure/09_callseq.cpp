#include <iostream>
#include <map>
#include <vector>
#include <utility>
#include <cctype>
#include <sstream>
#include <algorithm>

using namespace std;

void f_calling(vector<pair<char, string>>& sequence, char name, map<char, vector<string>> function, vector<char> history){ // 함수 호출
    history.push_back(name); // 호출한 함수 추가

    for(auto i : function[name]){
        if(i[0] == '$')
            break;

        else if(isupper(i[0])){ // 대문자 - 함수 호출
            if(find(history.begin(), history.end(), i[0]) != history.end()){
                cout << "DEADLOCK" << endl;
                exit(0);
            }
            else {
                f_calling(sequence, i[0], function, history);
            }
        }

        else{ // 소문자 - 수행문 수행
            sequence.push_back({name, i});
        }
    }
}

int main(){
    map<char, vector<string>> function; // 함수 이름과 그 수행문들로 구성된 map
    int num_function, select1, select2;
    cin >> num_function >> select1 >> select2;

    while(num_function--){ // 함수와 그 수행문 입력받기
        char name; // 함수 이름
        string perform; // 기능
        cin >> name;
        getline(cin, perform);
        istringstream iss(perform);

        vector<string> tokens;
        string token;

        while(iss >> token){ // 공백 기준으로 분리
            tokens.push_back(token);
        }
        function[name] = tokens;
    }

    vector<pair<char, string>> sequence; // 수행한 것들의 나열

    for(auto i : function['M']){
        if(i[0] == '$')
            break;
        else if(isupper(i[0])){ // 대문자 - 함수 호출
            f_calling(sequence, i[0], function, {'M'});
        }
        else{
            sequence.push_back({'M', i}); // 함수 이름과 수행하는 문장 추가
        }
    }

    int size = sequence.size();

    // 출력할차례
    for(auto i : {select1, select2}){
        if(size < i) // 사이즈를 초과했을 때
            cout << "NONE" << endl;
        else if(0 <= i){ // 사이즈 초과 안하고 0보다 클 때
            cout << sequence[i - 1].first << "-" << sequence[i - 1].second << endl;
        }
        else{ // 0보다 작을 때
            cout << sequence[size + i].first << "-" << sequence[size + i].second << endl;
        }
    }

    return 0;
}
