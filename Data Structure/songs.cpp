#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class SONG{ // SONG 클래스
private :
public :
    SONG(string, char, int, double, int);
    string name;
    char genre;
    int broad, download;
    double size;
};

SONG::SONG(string name, char genre, int broad, double size, int download) :
    name(name), genre(genre), broad(broad), size(size), download(download){};

bool makerank(SONG song1, SONG song2){
    if(song1.broad == song2.broad){
        if(song1.download == song2.download){
            return song1.size < song2.size ? true : false;
        }
        else
            return song1.download < song2.download ? false : true;
    }
    else
        return song1.broad < song2.broad ? false : true;
}

int main() {
    int num_songs, whichsong; // 노래 수, 어느 노래
    cin >> num_songs >> whichsong;

    string name;
    char genre;
    int broad, download;
    double size;
    vector<SONG> songs; // SONG클래스 배열

    for(int i = 0; i < num_songs; i++){ // 배열에 노래들 집어넣기
        cin >> name >> genre >> broad >> size >> download;
        songs.push_back(SONG(name, genre, broad, size, download));
    }

    sort(songs.begin(), songs.end(), makerank);  // 1,2,3 순위 정렬

    char beforegenre = ' ';
    vector<SONG> songs2;
    queue<SONG> temp;

    for(auto i = songs.begin(); i < songs.end(); i++){
        if(i->genre == beforegenre){ // 앞 순위와 장르가 같을 경우
            temp.push(*i);
        }
        else{ // 장르 다른 경우
            songs2.push_back(*i);
            beforegenre = i->genre;
            if(temp.size()) {
                songs2.push_back(temp.front());
                beforegenre = temp.front().genre;
                temp.pop();
            }
        }
    }

    if(temp.size()){
        for(int i = 0; i < temp.size(); i++){
            songs2.push_back(temp.front());
            temp.pop();
        }
    }

    cout << songs2[whichsong - 1].name;

    return 0;
}


