
window.addEventListener("load",function(){
    getlist();
    /*     let list = document.querySelector("list");
    list.innerHTML = <h1>로딩완료</h1>;
 */    
})

function getlist(){
    // 준비
    let xhr = new XMLHttpRequest();
    
    //// 세팅
    // 세팅
    //let url = "https://cors-anywhere.herokuapp.com/https://comic.naver.com/index";
    let url = "https://cors-anywhere.herokuapp.com/https://comic.naver.com/api/realtime/ranking/list?rankTabType=DEFAULT";
    xhr.open("get", url);
    
    // 실행
    xhr.send();

    // 얻어온 url 결과물을 갖고
    // 접속완료 이벤트가 실행
    xhr.onload = function(){
        let data = xhr.responseText;
        console.log("------------------------")
        console.log(data);
        console.log("------------------------")
    }
}
