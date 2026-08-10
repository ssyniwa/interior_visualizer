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
        "ボヘミアン (Bohemian)": {"type": "image", "path": "videos/living_bohemian.png"},
        "ミニマリスト (Minimalist)": {"type": "image", "path": "videos/living_minimalist.png"},
        "ブルックリン (Brooklyn)": {"type": "image", "path": "videos/living_brooklyn.png"},
        "フレンチシック (French Chic)": {"type": "image", "path": "videos/living_french.png"},
        "コースタル (Coastal)": {"type": "image", "path": "videos/living_coastal.png"},
        "レトロモダン (Mid-Century)": {"type": "image", "path": "videos/living_retro.png"},
        "サイバーパンク (Cyberpunk)": {"type": "image", "path": "videos/living_cyberpunk.png"},
        "バイオフィリック未来 (Biophilic)": {"type": "image", "path": "videos/living_biophilic.png"},
        "スペースエイジ (Space Age)": {"type": "image", "path": "videos/living_spaceage.png"},
        "ポストアポカリプス (Ruins)": {"type": "image", "path": "videos/living_ruins.png"},
        "ネオメンフィス (Neo-Memphis)": {"type": "image", "path": "videos/living_memphis.png"},
        "カラーポップ (Colorful)": {"type": "image", "path": "videos/living_colorful.png"},
        "ロック＆グランジ (Rock)": {"type": "image", "path": "videos/living_rock.png"},
        "アーバン・スタイリッシュ (Stylish)": {"type": "image", "path": "videos/living_stylish.png"},
        "寒冷地ロッジ (Alpine)": {"type": "image", "path": "videos/living_alpine.png"},
        "南国リゾート (Tropical)": {"type": "image", "path": "videos/living_tropical.png"},
        "魔法ファンタジー (Fantasy)": {"type": "image", "path": "videos/living_fantasy.png"},
        "研究所 (Laboratory)": {"type": "image", "path": "videos/living_lab.png"},
        "海中 (Underwater)": {"type": "image", "path": "videos/living_underwater.png"},
        "新緑の森 (Forest)": {"type": "image", "path": "videos/living_forest.png"},
        "星空 (Starry Sky)": {"type": "image", "path": "videos/living_starry.png"},
        "天空 (Sky Sanctuary)": {"type": "image", "path": "videos/living_sky.png"},
        "電子空間 (Cyberspace)": {"type": "image", "path": "videos/living_cyberspace.png"},
        "雷鳴 (Thunder)": {"type": "image", "path": "videos/living_thunder.png"},
        "日本庭園 (Japanese Garden)": {"type": "image", "path": "videos/living_japanesegarden.png"},
        "クリスタル (Crystal)": {"type": "image", "path": "videos/living_crystal.png"},
    },
    "ワークスペース (書斎)": {
        "北欧風 (Scandinavian)": {"type": "video", "path": "videos/work_scandi.mp4"},
        "モダン (Modern)": {"type": "video", "path": "videos/work_modern.mp4"},
        "インダストリアル (Industrial)": {"type": "video", "path": "videos/work_industrial.mp4"},
        "和モダン (Japandi)": {"type": "image", "path": "videos/work_japandi.png"},
        "ボヘミアン (Bohemian)": {"type": "image", "path": "videos/work_bohemian.png"},
        "ミニマリスト (Minimalist)": {"type": "image", "path": "videos/work_minimalist.png"},
        "ブルックリン (Brooklyn)": {"type": "image", "path": "videos/work_brooklyn.png"},
        "フレンチシック (French Chic)": {"type": "image", "path": "videos/work_french.png"},
        "コースタル (Coastal)": {"type": "image", "path": "videos/work_coastal.png"},
        "レトロモダン (Mid-Century)": {"type": "image", "path": "videos/work_retro.png"},
        "サイバーパンク (Cyberpunk)": {"type": "image", "path": "videos/work_cyberpunk.png"},
        "バイオフィリック未来 (Biophilic)": {"type": "image", "path": "videos/work_biophilic.png"},
        "スペースエイジ (Space Age)": {"type": "image", "path": "videos/work_spaceage.png"},
        "ポストアポカリプス (Ruins)": {"type": "image", "path": "videos/work_ruins.png"},
        "ネオメンフィス (Neo-Memphis)": {"type": "image", "path": "videos/work_memphis.png"},
        "カラーポップ (Colorful)": {"type": "image", "path": "videos/work_colorful.png"},
        "ロック＆グランジ (Rock)": {"type": "image", "path": "videos/work_rock.png"},
        "アーバン・スタイリッシュ (Stylish)": {"type": "image", "path": "videos/work_stylish.png"},
        "寒冷地ロッジ (Alpine)": {"type": "image", "path": "videos/work_alpine.png"},
        "南国リゾート (Tropical)": {"type": "image", "path": "videos/work_tropical.png"},
        "魔法ファンタジー (Fantasy)": {"type": "image", "path": "videos/work_fantasy.png"},
        "研究所 (Laboratory)": {"type": "image", "path": "videos/work_lab.png"},
        "海中 (Underwater)": {"type": "image", "path": "videos/work_underwater.png"},
        "新緑の森 (Forest)": {"type": "image", "path": "videos/work_forest.png"},
        "星空 (Starry Sky)": {"type": "image", "path": "videos/work_starry.png"},
        "天空 (Sky Sanctuary)": {"type": "image", "path": "videos/work_sky.jpg"},
        "電子空間 (Cyberspace)": {"type": "image", "path": "videos/work_cyberspace.png"},
        "雷鳴 (Thunder)": {"type": "image", "path": "videos/work_thunder.png"},
        "日本庭園 (Japanese Garden)": {"type": "image", "path": "videos/work_japanesegarden.png"},
        "クリスタル (Crystal)": {"type": "image", "path": "videos/work_crystal.png"},
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
        "レトロモダン (Mid-Century)",
        "サイバーパンク (Cyberpunk)",
        "バイオフィリック未来 (Biophilic)",
        "スペースエイジ (Space Age)",
        "ポストアポカリプス (Ruins)",
        "ネオメンフィス (Neo-Memphis)",
        "カラーポップ (Colorful)",
        "ロック＆グランジ (Rock)",
        "アーバン・スタイリッシュ (Stylish)",
        "寒冷地ロッジ (Alpine)",
        "南国リゾート (Tropical)",
        "魔法ファンタジー (Fantasy)",
        "研究所 (Laboratory)",
        "海中 (Underwater)",
        "新緑の森 (Forest)",
        "星空 (Starry Sky)",
        "天空 (Sky Sanctuary)",
        "電子空間 (Cyberspace)",
        "雷鳴 (Thunder)",
        "日本庭園 (Japanese Garden)",
        "クリスタル (Crystal)"
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
    elif style == "サイバーパンク (Cyberpunk)":
        st.markdown("""
        - **コンセプト:** ネオンと金属質が織りなす近未来の都市空間
        - **カラーパレット:** ネオンシアン、マゼンタ、クロームシルバー
        - **おすすめ家具:** 
            - LED発光ラインの家具
            - メッシュパネルの壁面
            - ホログラム風ディスプレイ
        """)
    elif style == "バイオフィリック未来 (Biophilic)":
        st.markdown("""
        - **コンセプト:** 自然とハイテクが融合した有機的な未来空間
        - **カラーパレット:** 発光グリーン、アースブラウン、クリアホワイト
        - **おすすめ家具:** 
            - 流線型の有機的なチェア
            - 壁面緑化システムと一体化した照明
        """)
    elif style == "スペースエイジ (Space Age)":
        st.markdown("""
        - **コンセプト:** レトロフューチャーな宇宙時代を彷彿とさせるポップな空間
        - **カラーパレット:** オレンジ、ビビッドレッド、ホワイト
        - **おすすめ家具:** 
            - 球体や卵型のプラスチック家具
            - ラウンドフレームのミラー
        """)
    elif style == "ポストアポカリプス (Ruins)":
        st.markdown("""
        - **コンセプト:** 文明崩壊後の世界を生き抜く退廃的シェルター風空間
        - **カラーパレット:** 錆色、コンクリートグレー
        - **おすすめ家具:** 
            - ひび割れたコンクリート壁
            - ドラム缶や古材を再利用したテーブル
        """)
    elif style == "ネオメンフィス (Neo-Memphis)":
        st.markdown("""
        - **コンセプト:** 奇抜な幾何学模様と偏光カラーが交差するアート空間
        - **カラーパレット:** オーロラカラー、パステルミント
        - **おすすめ家具:** 
            - 偏光（オーロラ）アクリルのテーブル
            - 非対称なブロックデザインのシェルフ
        """)
    elif style == "カラーポップ (Colorful)":
        st.markdown("""
        - **コンセプト:** 鮮やかな色彩と多彩な柄が溢れるエネルギッシュな空間
        - **カラーパレット:** ショッキングピンク、エメラルドグリーン、サンシャインイエロー
        - **おすすめ家具:** 
            - ベルベット素材のカラフルなソファ
            - 壁面ギャラリー（アート・小物）
        """)
    elif style == "ロック＆グランジ (Rock)":
        st.markdown("""
        - **コンセプト:** ライブハウスのバックステージを思わせる反逆的でカッコいい空間
        - **カラーパレット:** マットブラック、チャコール、バーガンディ
        - **おすすめ家具:** 
            - チェスターフィールドの黒革ソファ
            - スタッズ付き家具、アンプ型スピーカー
        """)
    elif style == "アーバン・スタイリッシュ (Stylish)":
        st.markdown("""
        - **コンセプト:** 都会的で洗練された高級ホテルのようなシャープな空間
        - **カラーパレット:** チャコールグレー、シルバー、ダークウォールナット
        - **おすすめ家具:** 
            - ガラス・大理石調のローテーブル
            - 間接照明を活かしたスタイリッシュなレイアウト
        """)
    elif style == "寒冷地ロッジ (Alpine)":
        st.markdown("""
        - **コンセプト:** 雪深い極寒の地で暖を取る、温もりと重厚感のある空間
        - **カラーパレット:** スノーホワイト、パインウッド、ディープフォレストグリーン
        - **おすすめ家具:** 
            - ムートンラグやファー素材のクッション
            - 薪ストーブ、天然木のウッドファニチャー
        """)
    elif style == "南国リゾート (Tropical)":
        st.markdown("""
        - **コンセプト:** 陽気な南国の楽園や高級ヴィラを思わせる開放的な空間
        - **カラーパレット:** サンドホワイト、ハイビスカスレッド、ターコイズ
        - **おすすめ家具:** 
            - バナナリーフやアバカ編みのリゾートチェア
            - 大型観葉植物（モンステラ等）
        """)
    elif style == "魔法ファンタジー (Fantasy)":
        st.markdown("""
        - **コンセプト:** 中世の魔法使いの隠れ家や、神秘的な魔法陣が漂う空間
        - **カラーパレット:** ディープパープル、ゴールド、ミスティックブルー
        - **おすすめ家具:** 
            - 重厚な古木のブックシェルフと大量の魔導書
            - 浮遊するキャンドルや発光するクリスタル・ポーション
        """)
    elif style == "研究所 (Laboratory)":
        st.markdown("""
        - **コンセプト:** 近未来の科学者やアルケミストの実験室をイメージした知的な空間
        - **カラーパレット:** クリーンホワイト、スチールシルバー、アクセントブルー
        - **おすすめ家具:** 
            - ガラスのフラスコやビーカー、モニター機器が並ぶ作業台
            - メタリックな高機能チェア、配線剥き出しのギミックシェルフ
        """)
    elif style == "海中 (Underwater)":
        st.markdown("""
        - **コンセプト:** 深海の水族館やドームの中にいるような、青のグラデーションが美しい空間
        - **カラーパレット:** ディープアクア、サンドカラー、パールホワイト
        - **おすすめ家具:** 
            - 流線型の泡（バブル）をモチーフにしたライトやガラス家具
            - サンゴ礁や水面を揺らぐ光を演出するプロジェクター照明
        """)
    elif style == "新緑の森 (Forest)":
        st.markdown("""
        - **コンセプト:** 木漏れ日が差し込む豊かな森の中にいるような、癒やしと生命力あふれる空間
        - **カラーパレット:** モスグリーン、アースブラウン、サンライトゴールド
        - **おすすめ家具:** 
            - 枝の質感を活かしたウッドチェアや切り株風のスツール
            - 豊富な観葉植物とフェイクツリー、蔦を這わせた壁面
        """)
    elif style == "星空 (Starry Sky)":
        st.markdown("""
        - **コンセプト:** 満天の夜空や天文台に包まれているような、ロマンチックで神秘的な空間
        - **カラーパレット:** ミッドナイトブルー、プラチナシルバー、オーロラカラー
        - **おすすめ家具:** 
            - 天体望遠鏡や月の満ち欠けを模したインテリアオブジェ
            - 天井に広がるプラネタリウム風の投射照明、ベロア調のダークソファ
        """)
    elif style == "天空 (Sky Sanctuary)":
        st.markdown("""
        - **コンセプト:** 雲の上の神殿や浮島にいるような、どこまでも開放的で清らかな空間
        - **カラーパレット:** スカイブルー、ピュアホワイト、ゴールド
        - **おすすめ家具:** 
            - 羽や雲をモチーフにした軽やかなファブリック
            - 白木を基調としたローベッド、光を透過するガラスのオブジェ
        """)
    elif style == "電子空間 (Cyberspace)":
        st.markdown("""
        - **コンセプト:** デジタルデータの海やプログラムの内部に入り込んだような、無機質で先進的な空間
        - **カラーパレット:** マトリックスグリーン、ピクセルブラック、エレクトリックブルー
        - **おすすめ家具:** 
            - ワイヤーフレームやデータストリームが流れる壁面ディスプレイ
            - ミニマルな幾何学デザインの金属製デスク
        """)
    elif style == "雷鳴 (Thunder)":
        st.markdown("""
        - **コンセプト:** 嵐のなかの落雷をモチーフにした、鋭くエネルギッシュでスタイリッシュな空間
        - **カラーパレット:** プラズマバイオレット、ストームグレー、フラッシュイエロー
        - **おすすめ家具:** 
            - 稲妻の軌道を模した間接照明やネオンチューブ
            - ダークメタリックなソリッド家具、高硬度ガラスのテーブル
        """)
    elif style == "日本庭園 (Japanese Garden)":
        st.markdown("""
        - **コンセプト:** 伝統的な枯山水や和の庭を室内で表現した、圧倒的な静寂と気品漂う空間
        - **カラーパレット:** 苔色、砂利ホワイト、檜（ひのき）のナチュラルウッド
        - **おすすめ家具:** 
            - 低重心な木製ローソファ、竹や和紙を用いた仕切り
            - 室内にミニチュアの庭や灯籠をあしらった癒やしのレイアウト
        """)
    elif style == "クリスタル (Crystal)":
        st.markdown("""
        - **コンセプト:** 鉱山や洞窟に眠る巨大な水晶結晶に囲まれた、透明感と神秘的な輝きを放つ空間
        - **カラーパレット:** クリスタルクリア、ローズピンク、アイリスパープル
        - **おすすめ家具:** 
            - 原石やジオード（晶洞）のインテリア置物
            - 乱反射するアクリルやガラスで統一されたファニチャー
        """)

# フッター
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Streamlit & AI Video Generation</p>", unsafe_allow_html=True)
