from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views import View
import cv2


# ログイン前ホーム画面
def home(request):
    pass


# ログイン・サインアップ関連
# サインアップ
def signup(request):
    pass


# ログイン
def login(request):
    pass


# ログアウト
def logout(request):
    pass


# ユーザホーム
def user_home(request):
    return render(request, 'pages/user_home.html')


# 検索条件入力
def search(request):
    pass


# 検索結果
def recommend(request):
    pass


# カメラページ
# ストリーミング画像・映像を表示するview
class Camera(View):
    def get(self, request):
        return render(request, 'pages/camera.html', {})


# カメラページ更新用関数
def video_feed_view():
    width = 500
    height = 639
    return lambda _: StreamingHttpResponse(
        generate_frame(width, height),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )


# フレーム生成・返却する処理
def generate_frame(screen_width, screen_height):
    # 画面サイズを取得する
    # screen_width = request.GET.get('screen_width', 1280)
    # screen_height = request.GET.get('screen_height', 720)

    capture = cv2.VideoCapture(0)  # USBカメラから

    # 解像度を変更する
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

    while True:
        if not capture.isOpened():
            print("Capture is not opened.")
            break
        # カメラからフレーム画像を取得
        ret, frame = capture.read()
        if not ret:
            print("Failed to read frame.")
            break
        # 縦横比を維持して縦幅を640ピクセルにリサイズする
        # ratio = frame.shape[1] / frame.shape[0]
        # resized_frame = cv2.resize(frame, (screen_width, screen_height))
        # フレーム画像バイナリに変換
        ret, jpeg = cv2.imencode('.jpg', frame)
        byte_frame = jpeg.tobytes()
        # フレーム画像のバイナリデータをユーザーに送付する
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + byte_frame + b'\r\n\r\n')
    capture.release()


# 撮った写真を表示
def lunch_photo(request):
    # Base64エンコードされた画像データ取得
    image = request.POST.get('image')
    print(image[:20])
    return render(request, 
                  'pages/lunch_photo.html', 
                  {'image': image})
