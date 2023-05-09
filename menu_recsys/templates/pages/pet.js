"use strict";

// カウンタ変数の初期化
var count = 0;
var pics_src = new Array("images/animal_01_g.png","images/animal_01_i.png");




// requestAnimationFrame()メソッドでループを実行
function loop() {
    // カウンタをインクリメント
    count++;

// キャンバス要素を取得する
const	ca = document.getElementById( "panda" );
var canvas = document.getElementById("myCanvas");
canvas.width = ca.clientWidth;
canvas.height = ca.clientHeight;

//console.log(ca.clientWidth)

// 2Dコンテキストを取得する
var ctx = canvas.getContext("2d");
var img_back = new Image();
img_back.src = "images/camp.png";//1920x1080




//var selimg = 0;

var img_g = new Image();//330x330
img_g.src = "images/animal_01_g.png";
var img_i = new Image();
img_i.src = "images/animal_01_i.png";

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



// function DrawMain()
// {
// 	const	g = gScreen.getContext( "2d" );				//	仮想画面の2D描画コンテキストを取得

// 	let		mx = Math.floor( gPlayerX / TILESIZE );			//	プレイヤーのタイル座標X
// 	let		my = Math.floor( gPlayerY / TILESIZE );			//	プレイヤーのタイル座標Y

// 	for( let dy = -SCR_HEIGHT; dy <= SCR_HEIGHT; dy++ ){
// 		let		ty = my + dy;								//	タイル座標Y
// 		let		py = ( ty + MAP_HEIGHT ) % MAP_HEIGHT;		//	ループ後タイル座標Y
// 		for( let dx = -SCR_WIDTH; dx <= SCR_WIDTH; dx++ ){
// 			let		tx = mx + dx;							//	タイル座標X
// 			let		px = ( tx + MAP_WIDTH  ) % MAP_WIDTH;	//	ループ後タイル座標X
// 			DrawTile( g,
// 			          tx * TILESIZE + WIDTH  / 2 - gPlayerX,
// 			          ty * TILESIZE + HEIGHT / 2 - gPlayerY,
// 			          gMap[ py * MAP_WIDTH + px ] );
// 		}
// 	}

// 	//	プレイヤー
// 	g.drawImage( gImgPlayer,
// 	             ( gFrame >> 4 & 1 ) * CHRWIDTH, gAngle * CHRHEIGHT, CHRWIDTH, CHRHEIGHT,
// 	             WIDTH / 2 - CHRWIDTH / 2, HEIGHT / 2 - CHRHEIGHT + TILESIZE / 2, CHRWIDTH, CHRHEIGHT );

// 	g.fillStyle = WNDSTYLE;							//	ウィンドウの色
// 	g.fillRect( 20, 103, 105, 15 );

// 	g.font = FONT;									//	文字フォントを設定
// 	g.fillStyle = FONTSTYLE;						//	文字色
// 	g.fillText( "x=" + gPlayerX + " y=" + gPlayerY + " m=" + gMap[ my * MAP_WIDTH + mx ], 25, 115 );
// }


// function DrawTile( g, x, y, idx )
// {
// 	const		ix = ( idx % TILECOLUMN ) * TILESIZE;
// 	const		iy = Math.floor( idx / TILECOLUMN ) * TILESIZE;
//     const	ca = document.getElementById( "main" );
// 	g.drawImage( gImgMap, 0, 0, 10000, 5000, 0, 0, ca.width, ca.height );
// }


// function LoadImage()
// {
// 	gImgMap    = new Image();	gImgMap.src    = gFileMap;		//	マップ画像読み込み
// 	gImgPlayer = new Image();	gImgPlayer.src = gFilePlayer;	//	プレイヤー画像読み込み
// }


// //	フィールド進行処理
// function TickField()
// {
// 	if( gMoveX != 0 || gMoveY != 0 ){}				//	移動中の場合
// 	else if( gKey[ 37 ] ){	gAngle = 1;	gMoveX = -TILESIZE;	}	//	左
// 	else if( gKey[ 38 ] ){	gAngle = 3;	gMoveY = -TILESIZE;	}	//	上
// 	else if( gKey[ 39 ] ){	gAngle = 2;	gMoveX =  TILESIZE;	}	//	右
// 	else if( gKey[ 40 ] ){	gAngle = 0;	gMoveY =  TILESIZE;	}	//	下

// 	//	移動後のタイル座標判定
// 	let		mx = Math.floor( ( gPlayerX + gMoveX ) / TILESIZE );	//	移動後のタイル座標X
// 	let		my = Math.floor( ( gPlayerY + gMoveY ) / TILESIZE );	//	移動後のタイル座標Y
// 	mx += MAP_WIDTH;								//	マップループ処理X
// 	mx %= MAP_WIDTH;								//	マップループ処理X
// 	my += MAP_HEIGHT;								//	マップループ処理Y
// 	my %= MAP_HEIGHT;								//	マップループ処理Y
// 	let		m = gMap[ my * MAP_WIDTH + mx ];		//	タイル番号
// 	if( m < 3 ){									//	侵入不可の地形の場合
// 		gMoveX = 0;									//	移動禁止X
// 		gMoveY = 0;									//	移動禁止Y
// 	}

// 	gPlayerX += Math.sign( gMoveX );				//	プレイヤー座標移動X
// 	gPlayerY += Math.sign( gMoveY );				//	プレイヤー座標移動Y
// 	gMoveX -= Math.sign( gMoveX );					//	移動量消費X
// 	gMoveY -= Math.sign( gMoveY );					//	移動量消費Y

// 	//	マップループ処理
// 	gPlayerX += ( MAP_WIDTH  * TILESIZE );
// 	gPlayerX %= ( MAP_WIDTH  * TILESIZE );
// 	gPlayerY += ( MAP_HEIGHT * TILESIZE );
// 	gPlayerY %= ( MAP_HEIGHT * TILESIZE );
// }


// function WmPaint()
// {
// 	DrawMain();

// 	const	ca = document.getElementById( "main" );	//	mainキャンバスの要素を取得
// 	const	g = ca.getContext( "2d" );				//	2D描画コンテキストを取得
// 	g.drawImage( gScreen, 0, 0, gScreen.width, gScreen.height, 0, 0, gWidth, gHeight );	//	仮想画面のイメージを実画面へ転送
// }


// //	ブラウザサイズ変更イベント
// function WmSize()
// {
// 	const	ca = document.getElementById( "main" );	//	mainキャンバスの要素を取得
//     // IDが "example" の要素を取得する例
//     let elementp = document.getElementById("panda");
//     ca.width = elementp.clientWidth;
//     ca.height= elementp.clientHeight;
// 	// ca.width = window.innerWidth;					//	キャンバスの幅をブラウザの幅へ変更
// 	// ca.height = window.innerHeight;					//	キャンバスの高さをブラウザの高さへ変更

// 	const	g = ca.getContext( "2d" );				//	2D描画コンテキストを取得
// 	g.imageSmoothingEnabled = g.msImageSmoothingEnabled = SMOOTH;	//	補間処理

// 	//	実画面サイズを計測。ドットのアスペクト比を維持したままでの最大サイズを計測する。
// 	gWidth = ca.width;
// 	gHeight = ca.height;
// 	if( gWidth / WIDTH < gHeight / HEIGHT ){
// 		gHeight = gWidth * HEIGHT / WIDTH;
// 	}else{
// 		gWidth = gHeight * WIDTH / HEIGHT;
// 	}
// }


// //	タイマーイベント発生時の処理
// function WmTimer()
// {
// 	gFrame++;						//	内部カウンタを加算
// 	TickField();					//	フィールド進行処理
// 	WmPaint();
// }


// //	キー入力(DONW)イベント
// window.onkeydown = function( ev )
// {
// 	let		c = ev.keyCode;			//	キーコード取得

// 	gKey[ c ] = 1;
// }


// //	キー入力(UP)イベント
// window.onkeyup = function( ev )
// {
// 	gKey[ ev.keyCode ] = 0;
// }


// //	ブラウザ起動イベント
// window.onload = function()
// {
// 	LoadImage();

// 	gScreen = document.createElement( "canvas" );	//	仮想画面を作成
// 	gScreen.width = WIDTH;							//	仮想画面の幅を設定
// 	gScreen.height = HEIGHT;						//	仮想画面の高さを設定

// 	WmSize();										//	画面サイズ初期化
// 	window.addEventListener( "resize", function(){ WmSize() } );	//	ブラウザサイズ変更時、WmSize()が呼ばれるよう指示
// 	setInterval( function(){ WmTimer() }, 33 );		//	33ms間隔で、WmTimer()を呼び出すよう指示（約30.3fps）
// }
