#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

/* 고객을 관리하는 class*/
class Client{
public :
    int id;
    int num_item;

    Client(int id, int num_item) : id(id), num_item(num_item){}
};

class Counter{
public :
    queue<Client> counter;
    int totalTime = 0;
    int uniqueNum;

    Counter(int num) : uniqueNum(num){}

    void f_plusClient(Client c){
        counter.push(c);
        totalTime += c.num_item;
    }

};


int main(){
    int num_client, num_counter;
    cin >> num_client >> num_counter;

    if(num_client < num_counter)
        num_counter = num_client;

    vector<Client> clients;
    int id, num_item;
    for(int i = 0; i < num_client; i++){ /* 고객 번호와 구매 물품 수 입력 함수 */
        cin >> id >> num_item;
        clients.push_back(Client(id, num_item));
    }

    vector<Counter> counters;

    for(int i = 0; i < num_counter; i++)
        counters.push_back(Counter(i));

    for(auto i : clients){
        counters[0].f_plusClient(i);
        sort(counters.begin(), counters.end(),
             [](Counter a, Counter b){if(a.totalTime == b.totalTime)
                 return a.uniqueNum < b.uniqueNum;
             else
                 return a.totalTime < b.totalTime;});
    }

    while(! counters.empty()){
        sort(counters.begin(), counters.end(),
             [](Counter a, Counter b){if(a.counter.front().num_item == b.counter.front().num_item) // 아이템 수 같으면
                 return a.uniqueNum > b.uniqueNum; // 더 큰 고유번호의 계산대가 앞으로 오게
             else
                 return a.counter.front().num_item < b.counter.front().num_item;}); // 아이템 수 다르면 더 작은 아이템 수의 계산대가 앞으로 오게});// 정렬

        Client temp = counters[0].counter.front(); // 가장 낮은거 선택
        counters[0].counter.pop(); // 가장 낮은거 제거

        cout << temp.id << endl; // 가장 낮은거 출력
        for(auto i = counters.begin() + 1; i < counters.end(); i++)
            i->counter.front().num_item -= temp.num_item;

        if(counters[0].counter.empty())
            counters.assign(counters.begin()+1, counters.end());

    }

    return 0;
}
