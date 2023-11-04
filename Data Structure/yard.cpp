#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

void f_pile_up(vector<stack<int>>& yard, vector<int> height){ // 적치하는 함수
    int max_height = *max_element(height.begin(), height.end());
    int min_height = *min_element(height.begin(), height.end()); // 가장 낮은 것은 높이가 같아도 어차피 앞의 것에 쌓으니 상관 없음
    int min_index = find(height.begin(), height.end(), min_height) - height.begin();
    int max_index = find(height.begin(), height.end(), max_height) - height.begin();
    int standard = 0;

    for(int i = max_index; i < yard.size(); i++){
        if(yard[i].size() == max_height)
            if(standard < yard[i].top()) {
                standard = yard[i].top();
                max_index = i;
            }
    }

    yard[min_index].push(yard[max_index].top()); // 가장 높은 곳에서 가장 낮은 곳으로 이동
    yard[max_index].pop();

}

int main(){
    int num_container; cin >> num_container; // 컨테이너 수 입력받기
    vector<stack<int>> yard(num_container); // 컨테이너 수 만큼 스택 생성

    for(int i = 0; i < num_container; i++){
        int num_elements;
        cin >> num_elements;
        int element;

        for(int j = 0; j < num_elements; j++){
            cin >> element;
            yard[i].push(element);
        }
    }

    vector<int> height; // 컨테이너별 높이

    for(auto i : yard)
        height.push_back(i.size());

    do{

        f_pile_up(yard, height);

        height = {};

        for(auto i : yard)
            height.push_back(i.size());
    }while(*max_element(height.begin(), height.end()) - *min_element(height.begin(), height.end()) != 1);  // 최대 높이 - 최소 높이 == 1일 때 종료

    vector<stack<int>> newyard(num_container);

    for(int i = 0; i < yard.size(); i++){
        while(! yard[i].empty()) {
            newyard[i].push(yard[i].top());
            yard[i].pop();
        }
    }

    for(auto i : newyard){
        while(i.size()){
            cout << i.top() << " ";
            i.pop();
        }
        cout << endl;
    }

    return 0;
}