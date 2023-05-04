# このファイルには画像処理関連の関数を書いていきます

from PIL import Image
import numpy as np
from google.cloud import vision
from google.oauth2 import service_account
import cv2
import imgsim

# 画像データを受け取る
# image: カメラから入力される想定 -> cv2.read()で読み込んだ画像
# https://qiita.com/takeshikondo/items/9e1664b15019160a0a5b
# 上記のページの「test6():」の実装中に、cv2.read()の結果をVision api に渡している部分が出てくる。
def object_detect(cv2_image):
    # 認証情報
    credentials = service_account.Credentials.from_service_account_file('key.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # 画像を読み込む
    img_rgb = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    _, enc_img = cv2.imencode(".jpg", img_rgb)
    content = enc_img.tostring()
    image = vision.Image(content=content)

    # 食堂メニュー全て取得
    # TODO: データベースから画像をとってくる
    # 今回はダミーデータで行くぞ
    dummy_menus = [
        "スクリーンショット 2023-05-04 9.14.52.png",
        "スクリーンショット 2023-05-04 9.15.07.png",
        "スクリーンショット 2023-05-04 9.15.42.png",
        "スクリーンショット 2023-05-04 9.29.04.png",
        # "スクリーンショット 2023-05-04 9.34.19.png",
        "スクリーンショット 2023-05-04 9.46.56.png",
        "スクリーンショット 2023-05-04 9.52.24.png",
        "スクリーンショット 2023-05-04 9.53.15.png"
    ]
    menus = [cv2.imread(f) for f in dummy_menus]
    vtr = imgsim.Vectorizer()
    menu_vecs = [vtr.vectorize(menu) for menu in menus]

    ordered_menus = []

    # 物体検知
    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        vertices = []
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
            vertices.append([vertex.x, vertex.y])
    
        # imageから検知されたオブジェクトを一個一個取り出して、食堂メニュー写真との類似度を比べる
        # 画像の切り抜き：https://stackoverflow.com/questions/75603351/how-to-draw-bounding-boxes-using-normalized-bounding-polygon-vertices 
        # vertex に入っているのは標準化されている座標なので、もとに戻す
        height, width = cv2_image.shape[:2]
        cropped_image = cv2_image[int(vertices[0][1] * height):int(vertices[2][1] * height), int(vertices[0][0] * width):int(vertices[1][0] * width)]

        # 食堂のメニューと照らし合わせて、どのメニューと最も似ているか判断
        # imgsim: https://qiita.com/paragasu/items/c2ad5403c1c3f2a2c810
        min_distance_id = 0
        min_distance = 1000
        vec0 = vtr.vectorize(cropped_image)
        for i, vec1 in enumerate(menu_vecs):
            dist = imgsim.distance(vec0, vec1)
            if dist < min_distance:
                min_distance = dist
                min_distance_id = i

        # 最も似ているメニューのDB中のidなどを保存
        cv2.imwrite(str(min_distance_id) + ".jpg", menus[min_distance_id])
        ordered_menus.append(min_distance_id)

    # 検出されたメニューid一覧をreturn
    return ordered_menus

image_path = './クリスマスランチ①.jpeg'
content = cv2.imread(image_path)
print(object_detect(content))
