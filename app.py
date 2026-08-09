import streamlit as st

# ページの設定
st.set_page_config(
    page_title="AI Interior Visualizer",
    page_icon="🛋️",
    layout="wide"
)

# タイトル
st.title("🛋️ AIインテリア・リフォームビジュアライザー")
st.markdown("お好みのスタイルや条件を選ぶだけで、AIが生成した標準的な部屋のリフォーム後イメージ動画を表示します。")

st.markdown("---")

# サイドバー：ユーザーの選択項目
st.sidebar.header("🎨 リフォーム条件の選択")

style = st.sidebar.selectbox(
    "インテリアスタイル",
    ["北欧風 (Scandinavian)", "モダン (Modern)", "インダストリアル (Industrial)", "和モダン (Japandi)"]
)

room_type = st.sidebar.selectbox(
    "部屋の種類",
    ["リビングルーム", "ワークスペース (書斎)"]
)

lighting = st.sidebar.radio(
    "照明・時間帯の雰囲気",
    ["🌙 夜間の暖色系間接照明"]
)

# 動画ファイルのパス（またはURL）のマッピング
# ※実際には、事前に生成したAI動画のファイルパスやクラウド上のURLを指定します
video_database = {
    "北欧風 (Scandinavian)": "https://www.w3schools.com/html/mov_bbb.mp4",  # サンプル用URL
    "モダン (Modern)": "https://www.w3schools.com/html/mov_bbb.mp4",
    "インダストリアル (Industrial)": "https://www.w3schools.com/html/mov_bbb.mp4",
    "和モダン (Japandi)": "https://www.w3schools.com/html/mov_bbb.mp4"
}

# メイン画面のレイアウト（2カラム構成）
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🎬 プレビュー: {style} / {room_type}")
    
    # 選択されたスタイルの動画を表示
    selected_video = video_database.get(style, "https://www.w3schools.com/html/mov_bbb.mp4")
    st.video(selected_video)
    
    st.caption(f"現在の設定: {lighting}でのシミュレーション映像")

with col2:
    st.subheader("💡 スタイルの特徴とポイント")
    
    if style == "北欧風 (Scandinavian)":
        st.markdown("""
        - **コンセプト:** 自然のぬくもりと機能性の調和
        - **カラーパレット:** ホワイト、ライトグレー、ペールウッド
        - **おすすめ家具:** 
            - パイン材やオーク材のローテーブル
            - グレーのファブリックソファ
            - ペンダンライト
        """)
    elif style == "モダン (Modern)":
        st.markdown("""
        - **コンセプト:** 無駄を削ぎ落とした洗練された空間
        - **カラーパレット:** モノトーン（黒・白・チャコール）
        - **おすすめ家具:** 
            - レザー調のソファ
            - ガラス天板のセンターテーブル
            - 埋め込み型のスマート照明
        """)
    elif style == "インダストリアル (Industrial)":
        st.markdown("""
        - **コンセプト:** ヴィンテージ感と無骨な素材感
        - **カラーパレット:** ブラックアイアン、レンガ色、ダークブラウン
        - **おすすめ家具:** 
            - スチール脚のウッドシェルフ
            - ブラックメタルのフロアランプ
        """)
    else:  # 和モダン (Japandi)
        st.markdown("""
        - **コンセプト:** 和の静寂と北欧の温かみの融合
        - **カラーパレット:** ベージュ、ウォールナット、墨色
        - **おすすめ家具:** 
            - ロータイプのウッドベッド・ソファ
            - 障子風の間仕切りや和紙の照明
        """)

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Streamlit & AI Video Generation</p>", unsafe_allow_html=True)
