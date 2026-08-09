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
video_database = {
    "リビングルーム": {
        "北欧風 (Scandinavian)": "videos/living_scandi.mp4",
        "モダン (Modern)": "videos/living_modern.mp4",
        "インダストリアル (Industrial)": "videos/living_industrial.mp4",
        "和モダン (Japandi)": "videos/living_japandi.mp4",
    },
    "ワークスペース (書斎)": {
        "北欧風 (Scandinavian)": "videos/work_scandi.mp4",
        "モダン (Modern)": "videos/work_modern.mp4",
        "インダストリアル (Industrial)": "videos/work_industrial.mp4",
        "和モダン (Japandi)": "videos/work_japandi.mp4",
    }
}
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

selected_video_path = video_database[room_type][style]

# メイン画面のレイアウト（2カラム構成）
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🎬 プレビュー: {room_type} / {style}")
    # 実際には動画ファイルへの正しいパスまたはURLを指定してください
    st.video(selected_video_path)
    
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
