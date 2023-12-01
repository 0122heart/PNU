#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> horizon, vertical; // 가로, 세로 배열 선언
    int sum_horizon = 0, sum_vertical = 0, hor, ver; // 총 가로 길이, 총 세로 길이 변수 선언


    while(1) {
        cin >> hor; // 가로 길이 받기
        if(hor) // 가로 길이가 0이 아니면 세로 길이 받기(0이면 종료임)
            cin >> ver;
        else
            break;
        horizon.push_back(hor); // 가로 벡터에 가로 요소 추가
        vertical.push_back(ver); // 세로 벡터에 세로 요소 추가
    }

    for(auto i : horizon)
        cout << "hor" << i << endl;
    for(auto i : vertical)
        cout << "ver" << i << endl;

    for(int i = 0; i < horizon.size(); i++){
        sum_horizon += horizon[i]; // 총 가로 길이 구하기
        sum_vertical += vertical[i]; // 총 세로 길이 구하기
    }

    vector<vector<int>> stair; // 좌표 표기를 위한 2차원 배열 선언, 0으로 초기화

    for(int i = 0; i < sum_vertical; i++){
        vector<int> temp(sum_horizon); // 가로 1차원 배열 선언
        stair.push_back(temp); // 2차원 배열 선언
    }

    ver = 0; hor = 0;

    for(int i = 0; i < horizon.size(); i++){ // 내부 영역을 1로 설정(외부 영역은 0)
        hor += horizon[i];
        for(int j = ver; j < ver + vertical[i]; j++)
            for(int k = 0; k < hor; k++)
                stair[j][k] = 1;
        ver += vertical[i];
    }

    int x, y;
    while(cin >> x){ // 입력이 있는 한 지속, x좌표 입력받기
        cin >> y; // y좌표 입력받기

        if((sum_horizon < x || sum_vertical < y) || (sum_horizon == x && vertical[vertical.size() - 1] < y) || (horizon[0] < x && sum_vertical == y))
            cout << "out";

        else if(sum_horizon == x || sum_vertical == y) { // 경계
            cout << "on";
        }

        else{ // 내부 or 걸칠 때
            if (stair[sum_vertical - y - 1][x]) // 내부
                cout << "in";


            else {
                if (stair[sum_vertical - y][x - 1]) // 경계
                    cout << "on";
                else
                    cout << "out";
            }
        }

        cout << endl;
    }

    return 0;
}
