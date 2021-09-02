## https://programmers.co.kr/learn/courses/30/lessons/81301

/*
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
*/


#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    string ans = "";
    for (int i=0; i<s.size(); i++){
        switch (s[i]){
            case 'z':
                ans += "0";
                i += 3;
                break;
            case 'o':
                ans += "1";
                i += 2;
                break;
            case 't':
                if (s[i+1] == 'w'){ans += "2"; i += 2;}
                else {ans += "3"; i += 4;}
                break;
            case 'f':
                if (s[i+1] == 'o'){ans += "4"; i += 3;}
                else {ans += "5"; i += 3;}
                break;
            case 's':
                if (s[i+1] == 'i'){ans += "6"; i += 2;}
                else {ans += "7"; i += 4;}
                break;
            case 'e':
                ans += "8";
                i += 4;
                break;
            case 'n':
                ans += "9";
                i += 3;
                break;
            default:
                ans += s[i];
                break;
        }
    }

    return std::stoi(ans);
}
