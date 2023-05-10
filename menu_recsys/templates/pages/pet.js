
"use strict";

// カウンタ変数の初期化
var count = 0;
var pics_src = new Array("images/animal_01_g.png","images/animal_01_i.png");




// requestAnimationFrame()メソッドでループを実行
function loop() {
    // カウンタをインクリメント
    count++;

// キャンバス要素を取得する
const	ca = document.getElementById( "user_home_panda" );
var canvas = document.getElementById("myCanvas");
canvas.width = ca.clientWidth;
canvas.height = ca.clientHeight;

//console.log(ca.clientWidth)

// 2Dコンテキストを取得する
var ctx = canvas.getContext("2d");
var img_back = new Image();
img_back.src = "{% static 'images/camp.png' %}";//1920x1080




//var selimg = 0;

var img_g = new Image();//330x330
img_g.src = "{% static 'images/animal_01_g.png' %}";
var img_i = new Image();
img_i.src = "{% static 'images/animal_01_i.png' %}";

     //var h_cat = img_back.height;
     //var w_cat = img_back.width;
 



var windwid = 1920;
var windhei = 1080;
//img_back.onload = function() {
    ctx.drawImage(img_back, 900 - (ca.clientWidth/2), 900 - ca.clientHeight, ca.clientWidth, ca.clientHeight, 0, 0, ca.clientWidth, ca.clientHeight);
//}




    // 四角形を描画する
// ctx.fillStyle = "red";
// ctx.fillRect(50, 50, 100+count, 100);

if ((count %80) > 40 ) {
    //img_g.onload = function() {
        ctx.drawImage(img_g, 0, 0, 330, 330, (ca.clientWidth/2) - (ca.clientHeight/6), ca.clientHeight*1/2, ca.clientHeight/3, ca.clientHeight/3);
    //};

} else {
    //img_i.onload = function() {
        ctx.drawImage(img_i, 0, 0, 330, 330, (ca.clientWidth/2) - (ca.clientHeight/6), ca.clientHeight*1/2, ca.clientHeight/3, ca.clientHeight/3);
    //};

}

//console.log(h_cat)

    // if ((count %80) < 40) {
    //     document.getElementById("mypic").src=pics_src[0];
    // } else {
    //     document.getElementById("mypic").src=pics_src[1];
    // }

    // if (count > 400){
    //     document.getElementById("mypic").src=pics_src[5];
    //     document.getElementById("mypic").left="600";
    // }
    



    // 次のフレームをリクエストする
    requestAnimationFrame(loop);
}



requestAnimationFrame(loop);

