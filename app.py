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
assets = {
    # assets辞書にリビング・ワークスペース用のパスを追加（適宜動画や画像のパスに変更してください）
    "リビングルーム": {
        "北欧風 (Scandinavian)": {"type": "video", "path": "videos/living_scandi.mp4"},
        "モダン (Modern)": {"type": "video", "path": "videos/living_modern.mp4"},
        "インダストリアル (Industrial)": {"type": "video", "path": "videos/living_industrial.mp4"},
        "和モダン (Japandi)": {"type": "video", "path": "videos/living_japandi.mp4"},
        "ボヘミアン (Bohemian)": {"type": "video", "path": "videos/living_bohemian.png"},
        "ミニマリスト (Minimalist)": {"type": "video", "path": "videos/living_minimalist.png"},
        "ブルックリン (Brooklyn)": {"type": "video", "path": "videos/living_brooklyn.png"},
        "フレンチシック (French Chic)": {"type": "video", "path": "videos/living_french.png"},
        "コースタル (Coastal)": {"type": "video", "path": "videos/living_coastal.png"},
        "レトロモダン (Mid-Century)": {"type": "video", "path": "videos/living_retro.png"},
    },
    "ワークスペース (書斎)": {
        "北欧風 (Scandinavian)": {"type": "video", "path": "videos/work_scandi.mp4"},
        "モダン (Modern)": {"type": "video", "path": "videos/work_modern.mp4"},
        "インダストリアル (Industrial)": {"type": "video", "path": "videos/work_industrial.mp4"},
        "和モダン (Japandi)": {"type": "image", "path": "videos/work_japandi.png"},
        "ボヘミアン (Bohemian)": {"type": "video", "path": "videos/work_bohemian.png"},
        "ミニマリスト (Minimalist)": {"type": "video", "path": "videos/work_minimalist.png"},
        "ブルックリン (Brooklyn)": {"type": "video", "path": "videos/work_brooklyn.png"},
        "フレンチシック (French Chic)": {"type": "video", "path": "videos/work_french.png"},
        "コースタル (Coastal)": {"type": "video", "path": "videos/work_coastal.png"},
        "レトロモダン (Mid-Century)": {"type": "video", "path": "videos/work_retro.png"},
    }
}
# サイドバー：ユーザーの選択項目
st.sidebar.header("🎨 リフォーム条件の選択")

style = st.sidebar.selectbox(
    "インテリアスタイル",
    [
        "北欧風 (Scandinavian)", 
        "モダン (Modern)", 
        "インダストリアル (Industrial)", 
        "和モダン (Japandi)",
        "ボヘミアン (Bohemian)",
        "ミニマリスト (Minimalist)",
        "ブルックリン (Brooklyn)",
        "フレンチシック (French Chic)",
        "コースタル (Coastal)",
        "レトロモダン (Mid-Century)"
    ]
)

room_type = st.sidebar.selectbox(
    "部屋の種類",
    ["リビングルーム", "ワークスペース (書斎)"]
)

lighting = st.sidebar.radio(
    "照明・時間帯の雰囲気",
    ["🌙 夜間の暖色系間接照明"]
)

selected_video_path = assets[room_type][style]

# メイン画面のレイアウト（2カラム構成）
col1, col2 = st.columns([2, 1])

# --- メイン画面での表示制御 ---
with col1:
    st.subheader(f"🎬 プレビュー: {room_type} / {style}")
    
    # 選択されたコンテンツ情報を取得
    content = assets[room_type][style]
    
    if content["type"] == "video":
        st.video(content["path"])
    else:
        # 画像を表示し、キャプションを追加
        st.image(content["path"], use_container_width=True)
        st.info("※ このスタイルは現在、静止画でのシミュレーションとなります。")
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
    elif style == "和モダン (Japandi)":
        st.markdown("""
        - **コンセプト:** 和の静寂と北欧の温かみの融合
        - **カラーパレット:** ベージュ、ウォールナット、墨色
        - **おすすめ家具:** 
            - ロータイプのウッドベッド・ソファ
            - 障子風の間仕切りや和紙の照明
        """)
    elif style == "ボヘミアン (Bohemian)":
        st.markdown("""
        - **コンセプト:** 自由で個性的な、色や素材をミックスした空間
        - **カラーパレット:** テラコッタ、マスタード、アースカラー
        - **おすすめ家具:** 
            - ラタン・籐素材のチェア
            - 民族柄のラグやクッション
            - ハンギングプランター
        """)
    elif style == "ミニマリスト (Minimalist)":
        st.markdown("""
        - **コンセプト:** 極限まで装飾を排した究極のシンプル
        - **カラーパレット:** ピュアホワイト、アイボリー、ライトグレー
        - **おすすめ家具:** 
            - 脚のすっきりしたローデザイン家具
            - 隠す収納のテレビボード
        """)
    elif style == "ブルックリン (Brooklyn)":
        st.markdown("""
        - **コンセプト:** 倉庫を思わせるラフで男前なヴィンテージスタイル
        - **カラーパレット:** レンガの赤茶、ダークグレー、古材ブラウン
        - **おすすめ家具:** 
            - ヴィンテージ風レザーソファ
            - パイプフレームのオープンシェルフ
        """)
    elif style == "フレンチシック (French Chic)":
        st.markdown("""
        - **コンセプト:** シャビーな風合いを残した大人の甘さを持つ空間
        - **カラーパレット:** アンティークホワイト、グレイッシュブルー
        - **おすすめ家具:** 
            - 猫脚のアンティーク風テーブル
            - ベルベット調のチェア
        """)
    elif style == "コースタル (Coastal)":
        st.markdown("""
        - **コンセプト:** カリフォルニアの海辺を感じる爽やかなリゾート空間
        - **カラーパレット:** オーシャンブルー、サンドベージュ、ホワイト
        - **おすすめ家具:** 
            - デニム生地のファブリックソファ
            - 流木や麻を使った小物
        """)
    elif style == "レトロモダン (Mid-Century)":
        st.markdown("""
        - **コンセプト:** 1950〜60年代のレトロな温かみを感じる空間
        - **カラーパレット:** マスタードイエロー、オリーブグリーン
        - **おすすめ家具:** 
            - ウッドフレームのパーソナルチェア
            - レトロなフロアランプ
        """)

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Streamlit & AI Video Generation</p>", unsafe_allow_html=True)
