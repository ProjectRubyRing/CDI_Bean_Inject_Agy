# -*- coding: utf-8 -*-
"""
generate_cdi_spec.py
CDI Bean Archive & @Inject Complete Specification Generator
Creates: CDI_BeanArchive_Complete_Specification.xlsx
Font: Meiryo UI (Strictly applied to 100% of cells)
Palette: Monotone Base (Professional Charcoal / Slate / Subtle Cool Gray)
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    # -------------------------------------------------------------------------
    # Design System & Monotone Palette
    # -------------------------------------------------------------------------
    FONT_NAME = "Meiryo UI"

    # Fonts
    font_sheet_title = Font(name=FONT_NAME, size=13, bold=True, color="FFFFFF")
    font_sheet_subtitle = Font(name=FONT_NAME, size=9.5, italic=True, color="4B5563")
    font_section_header = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
    font_table_header = Font(name=FONT_NAME, size=10, bold=True, color="FFFFFF")
    font_data = Font(name=FONT_NAME, size=9.5, color="1F2937")
    font_data_bold = Font(name=FONT_NAME, size=9.5, bold=True, color="111827")
    font_code = Font(name=FONT_NAME, size=9.5, color="111827")
    font_code_bold = Font(name=FONT_NAME, size=9.5, bold=True, color="111827")
    font_badge = Font(name=FONT_NAME, size=9, bold=True, color="FFFFFF")

    # Fills (Monotone / Slate Scale)
    fill_sheet_title = PatternFill(start_color="1F242D", end_color="1F242D", fill_type="solid")       # Dark Charcoal
    fill_sheet_subtitle = PatternFill(start_color="F3F4F6", end_color="F3F4F6", fill_type="solid")    # Soft Off-White Gray
    fill_section_header = PatternFill(start_color="374151", end_color="374151", fill_type="solid")    # Slate Charcoal
    fill_table_header = PatternFill(start_color="2D3748", end_color="2D3748", fill_type="solid")      # Deep Cool Charcoal
    fill_row_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
    fill_row_zebra = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")        # Very Subtle Cool Gray
    fill_highlight = PatternFill(start_color="E5E7EB", end_color="E5E7EB", fill_type="solid")        # Neutral Slate Gray Accent
    fill_badge_dark = PatternFill(start_color="1F2937", end_color="1F2937", fill_type="solid")

    # Borders
    thin_border_side = Side(style="thin", color="D1D5DB")
    border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    border_header = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    # Alignments
    align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    align_left_top = Alignment(horizontal="left", vertical="top", wrap_text=True)
    align_center_top = Alignment(horizontal="center", vertical="top", wrap_text=True)

    def apply_sheet_base(ws, freeze_cell="A6"):
        ws.views.sheetView[0].showGridLines = True
        ws.freeze_panes = freeze_cell

    # =========================================================================
    # TAB 1: 01_概要・たとえ話
    # =========================================================================
    ws1 = wb.create_sheet(title="01_概要・たとえ話")
    apply_sheet_base(ws1, "A6")

    ws1.merge_cells("A1:F1")
    ws1["A1"] = "【CDI超入門】なぜ @Inject が丸ごと効かないのか？ — 「学校の給食当番」でわかるBeanアーカイブと動作原理"
    ws1["A1"].font = font_sheet_title
    ws1["A1"].fill = fill_sheet_title
    ws1["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws1.row_dimensions[1].height = 40

    ws1.merge_cells("A2:F2")
    ws1["A2"] = "概要：Java/Jakarta EEのCDIでは、いくらクラスに @Inject や @ApplicationScoped を書いても、「Beanアーカイブ」として認識されていなければCDIコンテナは完全に無視します。その根本原因・歴史的背景・解決策を小学生でもわかる物語と技術仕様の両面から徹底解説します。"
    ws1["A2"].font = font_sheet_subtitle
    ws1["A2"].fill = fill_sheet_subtitle
    ws1["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws1.row_dimensions[2].height = 28

    # Section 1 Header
    ws1.merge_cells("A4:F4")
    ws1["A4"] = "第1章：小学生でも直感的にわかる「学校の給食当番」たとえ話対比表"
    ws1["A4"].font = font_section_header
    ws1["A4"].fill = fill_section_header
    ws1["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws1.row_dimensions[4].height = 28

    headers_tab1_sec1 = ["CDI用語 (専門用語)", "給食当番でのたとえ", "役割と動作イメージ", "もしコレが存在しなかったらどうなる？", "小学生向け超解説", "実務開発での教訓"]
    for col_idx, h in enumerate(headers_tab1_sec1, start=1):
        cell = ws1.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws1.row_dimensions[5].height = 26

    data_tab1_sec1 = [
        ("CDIコンテナ\n(Weld / ArC / OWB)", "給食の総責任者の先生", "教室を回って、誰が当番かを確認し、おかずやごはんの道具を届ける管理者。", "先生がいないと、当番が誰もお皿を受け取れず、給食がスタートしない。", "学校全体の給食を仕切る大人の先生です。この先生が見回りに来てくれないと、何も始まりません。", "CDIコンテナが管理していないインスタンス（newしたもの）には、先生は絶対に手を貸しません。"),
        ("Bean (CDI Bean)", "給食当番の生徒\n(ごはん係・おかず係)", "お仕事（ビジネスロジック）を実行するクラス。先生から任命されて働きます。", "普通の生徒（ただのJavaクラス）になり、給食の道具（依存オブジェクト）をもらえない。", "「今日のごはんを配る係」に任命された特別な生徒です。先生からお玉や食缶を受け取って仕事をします。", "CDIの管理下に入って初めてライフサイクル（生成〜破棄）やインターセプタが有効になります。"),
        ("Beanアーカイブ\n(beans.xmlのあるJAR/WAR)", "「給食当番参加クラス」\nのドアの看板", "「この教室（JAR）の中に給食当番がいますよ！」と先生に知らせるための参加証・公式看板。", "先生はその教室を「あそこは給食無関係の教室だ」と判断して完全に素通り（無視）する！", "教室のドアに貼る看板です。これが貼っていない教室は、先生はノックすらしてくれません。", "どれほど完璧なコードを書いても、BeanアーカイブでなければCDIエンジンから見れば存在しないも同然です。"),
        ("@Inject\n(インジェクション宣言)", "「おかずを配るスプーンを\nください！」という名札", "「私はこの仕事をするために、〇〇係（Serviceなど）が必要です」という要求サイン。", "名札がなければ先生は何も渡さない。しかし名札があっても看板がなければ先生に見てもらえない！", "「先生、私にお玉を渡して！」と胸に書いた名札です。先生が目の前に来てくれて初めて意味を持ちます。", "@Injectは『道具を要求する受け口』に過ぎず、スキャンされてコンテナが渡してくれないとnullのままです。"),
        ("NullPointerException\n(ヌルポ)", "お玉が届かず、空っぽの\n手でお盆を落として大惨事", "注入されるはずの変数が null のままメソッドを呼び出してしまい、プログラムが即死する。", "本番障害・システムクラッシュの最大の原因！", "スプーンがもらえると思って手を出したのに、先生が来なかったので手が空っぽ。空気をすくって大パニック！", "@Injectが効かない時の典型的症状No.1。呼び出し元または注入先がBeanアーカイブ外にいる証拠です。"),
        ("UnsatisfiedResolution\nException", "「そんな係の子はうちの学校に\n一人もいません！」と怒られる", "先生（CDI）が「@Injectの要求に合うBeanがクラスパスのどこにも見当たらない」と停止するエラー。", "アプリケーションの起動（デプロイ）自体が失敗し、サーバーが立ち上がらない。", "名札に「恐竜係を呼んで！」と書いたのに、先生が「そんな係の子は登録されてません！」と起動拒否する状態。", "注入先がBeanアーカイブになっていない、またはスコープアノテーションが欠落している時の典型的起動エラー。")
    ]

    for row_idx, row_data in enumerate(data_tab1_sec1, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws1.row_dimensions[row_idx].height = 48
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws1.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2] else align_left_top

    # Section 2 Header
    ws1.merge_cells("A13:F13")
    ws1["A13"] = "第2章：事件の深層 — なぜ「@Inject」と書いたのに完全に無視されるのか？"
    ws1["A13"].font = font_section_header
    ws1["A13"].fill = fill_section_header
    ws1["A13"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws1.row_dimensions[13].height = 28

    headers_tab1_sec2 = ["フェーズ", "開発者の思い込み (期待)", "JVM / CDIコンテナの冷酷な現実", "なぜすれ違いが起きるのか？", "発生する具体的な症状", "解決のための鉄則"]
    for col_idx, h in enumerate(headers_tab1_sec2, start=1):
        cell = ws1.cell(row=14, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws1.row_dimensions[14].height = 26

    data_tab1_sec2 = [
        ("1. ビルド・配置時", "「アノテーションを書いたから、フレームワークがよしなに自動検出してくれるはず」", "CDIコンテナは『Beanアーカイブの目印（beans.xml等）』のないJARやフォルダはスキャン対象から除外する。", "Javaには何万ものクラスが存在するため、全クラスを調べると起動時間が数十分かかる。だから明示フラグが必要。", "ビルドは通る（コンパイルエラーにはならない）ため、ミスに気付きにくい。", "ライブラリJARやWebモジュールに必ず正しい beans.xml を配置する。"),
        ("2. コンテナ起動時\n(型解決フェーズ)", "「@ApplicationScoped があるから、DIコンテナに登録されているはず」", "BeanアーカイブでないJARの中にクラスがある場合、コンテナはそのアノテーションを一切読み取らない。", "クラスファイルが存在していても、メタデータ登録ツリー（BeanManager）に追加されない。", "UnsatisfiedResolutionException が発生してサーバー起動がクラッシュする。", "注入対象のクラスがBeanアーカイブに含まれているかディレクトリ構成を確認する。"),
        ("3. 実行時\n(メソッド呼出時)", "「new MyService() しても、中に @Inject があるから自動で入るはず」", "new演算子は純粋なJVMのメモリ確保命令であり、CDIコンテナの割り込みコードは一切走らない。", "CDIは『コンテナが生成した時』だけフィールドに値を注入する。手動newされたオブジェクトはただのJavaオブジェクト。", "service.doSomething() を呼んだ瞬間に NullPointerException が炸裂する。", "呼び出し元の親クラス自身も必ず @Inject でCDIコンテナから取得する。絶対にnewしない！"),
        ("4. CDI 4.0移行時\n(最新の罠)", "「beans.xml を空っぽで置いてあるから、今まで通り全クラスが対象になるはず」", "CDI 4.0 (Jakarta EE 10) から、空のbeans.xmlの解釈が 'all' から 'annotated' へ変更された！", "過去のバージョン（CDI 1.1〜3.0）のノウハウのままだと、スコープ未指定のクラスが丸ごと除外される。", "今まで動いていたアプリをバージョンアップした瞬間、突然全インジェクションが停止する。", "beans.xml に bean-discovery-mode=\"annotated\" を意識し、全Beanにスコープを明記する。")
    ]

    for row_idx, row_data in enumerate(data_tab1_sec2, start=15):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws1.row_dimensions[row_idx].height = 50
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws1.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1] else align_left_top

    # Section 3: Summary Rules
    ws1.merge_cells("A20:F20")
    ws1["A20"] = "第3章：小学生でも守れる「CDIの絶対ルール 3箇条」"
    ws1["A20"].font = font_section_header
    ws1["A20"].fill = fill_section_header
    ws1["A20"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws1.row_dimensions[20].height = 28

    rules_data = [
        ("ルール 1", "【看板を立てよ】", "コードを書く前に、必ず META-INF/beans.xml（WARなら WEB-INF/beans.xml）を置くこと。看板のない教室は先生から透明人間扱いされます。"),
        ("ルール 2", "【名札には係（スコープ）を書け】", "クラスの上に @ApplicationScoped や @RequestScoped などのスコープを必ず書くこと。@Inject だけ書いても、自分の身元（スコープ）がないと参加できません。"),
        ("ルール 3", "【自分で勝手に new するな】", "CDIの世界では new は禁止。先生（CDIコンテナ）にお願いして @Inject で持ってきてもらうこと。自分で作ったロボットには魔法はかかりません。")
    ]
    for idx, (r_no, r_title, r_desc) in enumerate(rules_data, start=21):
        ws1.row_dimensions[idx].height = 36
        c1 = ws1.cell(row=idx, column=1, value=r_no)
        c1.font = font_data_bold
        c1.fill = fill_highlight
        c1.alignment = align_center
        c1.border = border_cell

        c2 = ws1.cell(row=idx, column=2, value=r_title)
        c2.font = font_data_bold
        c2.fill = fill_highlight
        c2.alignment = align_center
        c2.border = border_cell

        ws1.merge_cells(start_row=idx, start_column=3, end_row=idx, end_column=6)
        c3 = ws1.cell(row=idx, column=3, value=r_desc)
        c3.font = font_data
        c3.fill = fill_row_white
        c3.alignment = align_left
        for col_k in range(3, 7):
            ws1.cell(row=idx, column=col_k).border = border_cell

    col_widths_1 = {1: 18, 2: 24, 3: 34, 4: 34, 5: 36, 6: 38}
    for col_idx, w in col_widths_1.items():
        ws1.column_dimensions[get_column_letter(col_idx)].width = w

    # =========================================================================
    # TAB 2: 02_歴史と背景
    # =========================================================================
    ws2 = wb.create_sheet(title="02_歴史と背景")
    apply_sheet_base(ws2, "A6")

    ws2.merge_cells("A1:G1")
    ws2["A1"] = "【歴史と背景】なぜ「Beanアーカイブ（beans.xml）」という面倒な仕組みが必要だったのか？"
    ws2["A1"].font = font_sheet_title
    ws2["A1"].fill = fill_sheet_title
    ws2["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.row_dimensions[1].height = 40

    ws2.merge_cells("A2:G2")
    ws2["A2"] = "時代背景の解説：CDIが登場した2009年から、クラウド・コンテナ・GraalVMネイティブが主流となった最新のCDI 4.0 (Jakarta EE 10/11) に至るまで、「起動速度・メモリ効率」と「開発生産性」の果てしないせめぎ合いの歴史を紐解きます。"
    ws2["A2"].font = font_sheet_subtitle
    ws2["A2"].fill = fill_sheet_subtitle
    ws2["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.row_dimensions[2].height = 28

    # Section 1 Header
    ws2.merge_cells("A4:G4")
    ws2["A4"] = "第1章：CDIバージョン変遷とBeanアーカイブ規定の進化年表"
    ws2["A4"].font = font_section_header
    ws2["A4"].fill = fill_section_header
    ws2["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.row_dimensions[4].height = 28

    headers_tab2 = ["バージョン", "策定年・仕様", "Beanアーカイブの規定", "空のbeans.xmlの解釈", "なぜその仕様になったのか？（設計思想と背景）", "発生した問題・開発者の苦悩", "最新の意義と影響"]
    for col_idx, h in enumerate(headers_tab2, start=1):
        cell = ws2.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws2.row_dimensions[5].height = 26

    data_tab2 = [
        ("CDI 1.0\n(JSR 299)", "2009年\nJava EE 6", "【厳格必須】\nbeans.xml が存在しなければ絶対にBeanアーカイブとみなさない。", "bean-discovery-mode の概念なし\n（実質 all 相当）",
         "【クラスパス爆発の防止】\nエンタープライズJavaでは数百個のサードパーティJAR（数百MB）が存在。無条件に全クラスをスキャンすると起動に数分〜数十分を要しPermGenメモリが枯渇するため、明示的オプトインを必須にした。",
         "「中身が空っぽのXMLをわざわざWEB-INFやMETA-INFに置かないとDIが動かないのは面倒すぎる」「Springは不要なのに！」と不満が噴出した。",
         "Beanアーカイブという境界概念を確立。安全性を最優先した原点のアーキテクチャ。"),

        ("CDI 1.1 / 1.2\n(JSR 346)", "2013年\nJava EE 7", "【暗黙的アーカイブ導入】\nbeans.xmlがなくても、スコープアノテーションがあれば自動認識。bean-discovery-mode属性の登場。", "互換性維持のため\n「all」として扱われる\n(全クラスがBean候補)",
         "【利便性の追求と開発生産性の向上】\nSpring Boot等の台頭に対抗し、「設定ファイルゼロ」でアノテーション駆動開発を可能にするため、暗黙的アーカイブ（Implicit Bean Archive）を仕様化した。",
         "【本質問の根本原因の誕生】\n「beans.xmlがない場合、Bean定義アノテーションのないクラスはスキャンされない」という隠れたルールが生まれ、@Injectだけ付いたクラスが黙って無視される悲劇が多発した。",
         "bean-discovery-mode（all / annotated / none）の3値モデルが確立された。"),

        ("CDI 2.0\n(JSR 365)", "2017年\nJava EE 8", "【Java SE標準化】\nJava SE環境でSeContainerInitializerによる単体起動が可能に。<trim/>要素の導入。", "互換性維持のため\n「all」のまま維持",
         "【マイクロサービス化と軽量化】\n重厚なアプリケーションサーバー不要で、軽量なJavaプロセスとしてCDIを動かす要求に対応。不要なBeanをビルド時に削るトリミング機能が実験導入された。",
         "依然として空のbeans.xmlは 'all' だったため、意図しないライブラリ内部のクラスまでBean化されてメモリ消費が増大する課題が残った。",
         "Java SEでのCLIツールや軽量デーモンでCDIが広く使われる基盤となった。"),

        ("CDI 3.0\n(Jakarta EE 9)", "2020年\nJakarta EE 9", "【パッケージ名の移行】\njavax.enterprise → jakarta.enterprise\njavax.inject → jakarta.inject", "「all」のまま維持\n(移行の混乱防止のため動作仕様は維持)",
         "【OracleからEclipse財団への移管】\n商標問題によりjavaxパッケージが使用不可能となり、jakartaパッケージへの大規模置換が行われた。機能変更は最小限に抑えられた。",
         "パッケージ名の一斉書き換えツールが必要となり、古いライブラリと新しいライブラリが混在するとクラスロードやDIが壊れる事態が発生した。",
         "Jakarta EEエコシステムの基礎が確立された。"),

        ("CDI 4.0\n(Jakarta EE 10)", "2022年\nJakarta EE 10", "【劇的転換：CDI Liteの分離と空XMLの挙動変更】\n空のbeans.xmlのデフォルトが 'all' から 'annotated' へ変更！", "【破壊的変更】\n「annotated」に変更！\n(スコープなしクラスは無視)",
         "【クラウドネイティブ・AOT最適化】\nQuarkusやHelidon等によるGraalVMネイティブコンパイルや起動0.1秒が至上命題に。リフレクション不要なCDI Lite（ビルド互換拡張）を策定し、無駄な全クラススキャン（all）を事実上廃止した。",
         "過去の資産（Java EE 7/8時代）をそのまま移行すると、スコープを書いていなかったBeanが一斉に消滅し、UnsatisfiedResolutionException で起動不能になる移行障害が多発した。",
         "現代のJava開発におけるデファクトスタンダード。高速起動・低メモリ消費のための厳格化。"),

        ("CDI 4.1\n(Jakarta EE 11)", "2024年〜最新\nJakarta EE 11", "【CDI Liteの機能拡充】\n言語機能（Java 21のレコード・仮想スレッド）親和性向上とビルド時型検証のさらなる強化。", "「annotated」が標準\n(all は非推奨・非推奨化の流れ)",
         "【最新Javaの言語機能との完全統合】\nRecordsやSealed Classesのインジェクション、仮想スレッド下でのコンテキスト伝播の最適化。AOT（事前解析）によるエラーの事前検出を極限まで高める方向へ。",
         "実行時リフレクションに依存した古いCDI拡張（Portable Extensions）がCDI Lite環境で動作しないため、Build Compatible Extensionsへの書き換えが必要。",
         "コンテナ時代において最速・最小フットプリントを実現する次世代CDI基盤。")
    ]

    for row_idx, row_data in enumerate(data_tab2, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws2.row_dimensions[row_idx].height = 68
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws2.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2] else align_left_top

    # Section 2: Deep dive narrative
    ws2.merge_cells("A13:G13")
    ws2["A13"] = "第2章：深堀り考察 — なぜ「全部勝手にスキャン」してはいけないのか？（技術的真因）"
    ws2["A13"].font = font_section_header
    ws2["A13"].fill = fill_section_header
    ws2["A13"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws2.row_dimensions[13].height = 28

    headers_tab2_sec2 = ["論点・課題", "もし全クラスを無条件スキャンしたら？（仮定）", "技術的な弊害・リソースへの悪影響", "CDI設計者が下したアーキテクチャ判断", "現在（CDI 4.0）における解決の境地"]
    ws2.merge_cells("E14:G14")
    for col_idx, h in enumerate(headers_tab2_sec2[:4], start=1):
        cell = ws2.cell(row=14, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    c_last = ws2.cell(row=14, column=5, value=headers_tab2_sec2[4])
    c_last.font = font_table_header
    c_last.fill = fill_table_header
    c_last.alignment = align_center
    c_last.border = border_header
    for ck in [6, 7]:
        ws2.cell(row=14, column=ck).border = border_header
    ws2.row_dimensions[14].height = 26

    deep_data = [
        ("1. クラスローディングと起動時間", "クラスパス上の数万〜数十万の.classバイトコードを全て読み込み、ASM等でアノテーション解析を行う。", "起動時間が数秒から数十秒・数分へと跳ね上がる。コンテナのコールドスタート（サーバーレス等）が絶望的になる。", "JARのルートにある beans.xml をチェックし、存在しないJARのバイトコード読み込みを即座にスキップする境界を設けた。", "CDI Liteの導入により、実行時スキャンを捨て、Maven/Gradleコンパイル時にBeanを確定させるAOTビルドを実現。"),
        ("2. メモリ消費量\n(Metaspace / Heap)", "全クラスに対してコンテナ内部の Bean<?> メタデータインスタンスや InjectionPoint オブジェクトを構築する。", "Metaspace（旧PermGen）およびJVMヒープを数百MB消費。不要なクラスまでガベージコレクション対象外としてメモリに常駐する。", "bean-discovery-mode=\"annotated\" を導入し、スコープが明示されたクラス以外はメタデータを作らないように制限した。", "空のbeans.xmlでもデフォルトを \"annotated\" にすることで、意図しないメタデータ肥大化を根本から遮断した。"),
        ("3. 予期せぬBean競合と副作用", "3rdパーティライブラリ（Apache Commons等）に含まれる無関係なクラスまで勝手にCDI Beanとして登録されてしまう。", "型解決（Type-Safe Resolution）時に AmbiguousResolutionException が発生したり、デフォルトコンストラクタが勝手に呼ばれて例外が発生。", "Beanアーカイブの境界を設け、明示的にCDI連携を意図したモジュールのみをコンテナの制御下に置く原則を徹底した。", "プログラマが意図して @ApplicationScoped などを付与したクラスのみをBeanとする健全なエコシステムへ収束した。")
    ]

    for row_idx, r in enumerate(deep_data, start=15):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws2.row_dimensions[row_idx].height = 56
        for col_idx in range(1, 5):
            cell = ws2.cell(row=row_idx, column=col_idx, value=r[col_idx-1])
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx == 1 else align_left_top
        
        ws2.merge_cells(start_row=row_idx, start_column=5, end_row=row_idx, end_column=7)
        cell_m = ws2.cell(row=row_idx, column=5, value=r[4])
        cell_m.font = font_data
        cell_m.fill = fill_curr
        cell_m.alignment = align_left_top
        for ck in range(5, 8):
            ws2.cell(row=row_idx, column=ck).border = border_cell

    col_widths_2 = {1: 16, 2: 16, 3: 26, 4: 24, 5: 36, 6: 34, 7: 34}
    for col_idx, w in col_widths_2.items():
        ws2.column_dimensions[get_column_letter(col_idx)].width = w

    # =========================================================================
    # TAB 3: 03_アーカイブ分類と動作モード
    # =========================================================================
    ws3 = wb.create_sheet(title="03_アーカイブ分類と動作モード")
    apply_sheet_base(ws3, "A6")

    ws3.merge_cells("A1:F1")
    ws3["A1"] = "【徹底比較】Beanアーカイブの全3分類 × 動作モード × スコープアノテーション完全仕様"
    ws3["A1"].font = font_sheet_title
    ws3["A1"].fill = fill_sheet_title
    ws3["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws3.row_dimensions[1].height = 40

    ws3.merge_cells("A2:F2")
    ws3["A2"] = "分類と挙動の完全マトリクス：アーカイブの種類（明示的・暗黙的・非アーカイブ）と、bean-discovery-modeの指定値（annotated / all / none）、および「Bean定義アノテーション」に該当するか否かの判定一覧です。"
    ws3["A2"].font = font_sheet_subtitle
    ws3["A2"].fill = fill_sheet_subtitle
    ws3["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws3.row_dimensions[2].height = 28

    # Section 1
    ws3.merge_cells("A4:F4")
    ws3["A4"] = "第1章：Beanアーカイブの3大分類定義"
    ws3["A4"].font = font_section_header
    ws3["A4"].fill = fill_section_header
    ws3["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws3.row_dimensions[4].height = 28

    headers_tab3_sec1 = ["分類名", "定義条件 (ファイル構成)", "スキャン対象となるクラス", "CDIコンテナの認識動作", "代表的なユースケース", "注意すべきリスク・落とし穴"]
    for col_idx, h in enumerate(headers_tab3_sec1, start=1):
        cell = ws3.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws3.row_dimensions[5].height = 26

    data_tab3_sec1 = [
        ("明示的Beanアーカイブ\n(Explicit Bean Archive)", "META-INF/beans.xml（WARはWEB-INF/beans.xml）が存在し、bean-discovery-mode が \"all\" または \"annotated\"、あるいは属性未指定。",
         "モードに依存：\n・all の場合：アーカイブ内の全クラス（アノテーションなしも含む）\n・annotated の場合：Bean定義アノテーション付きクラスのみ",
         "CDI仕様のフル機能（インターセプタ、デコレータ、オルタナティブ、拡張機能）が完全に有効化される。",
         "自作のアプリケーションモジュール（WARのWEB-INF/classes、自作共通JARライブラリ）。",
         "CDI 4.0では空のbeans.xmlが 'annotated' 扱いになるため、スコープを書いていないクラスが脱落する点に厳重注意。"),

        ("暗黙的Beanアーカイブ\n(Implicit Bean Archive)", "beans.xml が存在しないが、クラスパス上に「Bean定義アノテーション」が付与されたクラスが1つ以上含まれるJAR/ディレクトリ。",
         "「Bean定義アノテーション」が付いたクラスのみ！\n（アノテーションのないクラスや、@Injectだけのクラスは完全に除外される）",
         "bean-discovery-mode=\"annotated\" と全く同じ挙動でスキャンされる。beans.xml内のタグ（interceptors等）は使えない。",
         "サードパーティ製のCDI対応ライブラリ（DeltaSpikeの一部、JAX-RSリソースライブラリ等）。",
         "【最大の罠】クラスに @Inject しか書いておらず @ApplicationScoped を忘れると、暗黙アーカイブの検出条件を満たさず非Bean扱いになる！"),

        ("非Beanアーカイブ\n(Non-Bean Archive)", "① beans.xml が存在せず、Bean定義アノテーション付きクラスも皆無のJAR\n② または beans.xml で bean-discovery-mode=\"none\" を明記したアーカイブ。",
         "【一切スキャンされない】\n含まれる全クラスがCDIコンテナから完全に無視される。",
         "CDIコンテナはアーカイブを完全にスキップ。メモリやスキャン時間を一切消費しない。",
         "Apache Commons、Logback、Jackson、JDBCドライバなどの一般的な非CDI Javaライブラリ。",
         "この中にあるクラスを誤って @Inject しようとすると、確実に UnsatisfiedResolutionException または NPE が発生する。")
    ]

    for row_idx, r in enumerate(data_tab3_sec1, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws3.row_dimensions[row_idx].height = 58
        for col_idx, val in enumerate(r, start=1):
            cell = ws3.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx == 1 else align_left_top

    # Section 2: bean-discovery-mode Comparison
    ws3.merge_cells("A10:F10")
    ws3["A10"] = "第2章：bean-discovery-mode 設定値の完全比較マトリクス"
    ws3["A10"].font = font_section_header
    ws3["A10"].fill = fill_section_header
    ws3["A10"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws3.row_dimensions[10].height = 28

    headers_tab3_sec2 = ["bean-discovery-mode 設定値", "CDI 1.1〜3.0 での動作", "CDI 4.0 / 4.1 (最新) での動作", "アノテーションなしクラスの扱い", "@Injectのみ付いたクラスの扱い", "推奨度と実務上の指針"]
    for col_idx, h in enumerate(headers_tab3_sec2, start=1):
        cell = ws3.cell(row=11, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws3.row_dimensions[11].height = 26

    data_tab3_sec2 = [
        ("bean-discovery-mode=\"annotated\"", "Bean定義アノテーションを持つクラスのみをBean候補として登録。", "左と同じ（CDI仕様の標準・最推奨モード）。",
         "完全に無視（Beanにならない）。", "【無視される】\nクラスにスコープがなければBeanにならないため注入不可。", "【最高（★★★★★）】\n現代のデファクトスタンダード。意図しないBean化を防ぎ、起動速度が最速。"),

        ("bean-discovery-mode=\"all\"", "アーカイブ内の全クラスをBean候補として登録（スコープなしは@Dependent扱い）。", "左と同じ（下位互換のために残されているが、CDI Lite等では非推奨）。",
         "自動的に @Dependent スコープのBeanとして登録される。", "Beanとして登録されるため、正常にインジェクション可能。", "【注意（★★☆☆☆）】\n意図しない大量のクラスがBean化されメモリ浪費・起動遅延を招く。レガシー保守専用。"),

        ("bean-discovery-mode=\"none\"", "CDIコンテナはこのアーカイブを完全に無視する。", "左と同じ（明示的な無効化）。",
         "完全に無視。", "完全に無視（CDI管理外）。", "【特定用途（★★★☆☆）】\nCDIスキャンを完全に遮断したい巨大JARや、自前でファクトリ管理したいモジュールに指定。"),

        ("【属性省略・空のbeans.xml】\n<beans ...> </beans>", "互換性維持のため\n「all」として動作した！\n(スコープなしでもBeanになった)", "【破壊的変更】\n「annotated」として動作する！\n(スコープなしクラスは突如除外)",
         "CDI 1.1〜3.0：@Dependent扱い\nCDI 4.0：完全に無視！", "CDI 1.1〜3.0：動いていた\nCDI 4.0：動かなくなり障害発生！", "【要注意（★☆☆☆☆）】\nバージョンアップ時の最大落とし穴。属性を省略せず、必ず明示的に annotated と書くべき。")
    ]

    for row_idx, r in enumerate(data_tab3_sec2, start=12):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws3.row_dimensions[row_idx].height = 52
        for col_idx, val in enumerate(r, start=1):
            cell = ws3.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 6] else align_left_top

    # Section 3: Bean Defining Annotation Table
    ws3.merge_cells("A17:F17")
    ws3["A17"] = "第3章：「Bean定義アノテーション（Bean Defining Annotation）」完全判定リスト"
    ws3["A17"].font = font_section_header
    ws3["A17"].fill = fill_section_header
    ws3["A17"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws3.row_dimensions[17].height = 28

    headers_tab3_sec3 = ["アノテーション名", "パッケージ (Jakarta / JavaEE)", "Bean定義として認識されるか？", "スコープの種類と生存期間", "なぜそう規定されているのか？", "開発者が陥る落とし穴"]
    for col_idx, h in enumerate(headers_tab3_sec3, start=1):
        cell = ws3.cell(row=18, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws3.row_dimensions[18].height = 26

    data_tab3_sec3 = [
        ("@ApplicationScoped", "jakarta.enterprise.context\n(javax.enterprise.context)", "〇 認識される\n(Bean定義)", "通常スコープ (Normal Scope)\nアプリケーション起動〜終了まで単一共有", "アプリ全体で共有するシングルトン的なサービス層・キャッシュを定義するため。", "クライアントプロキシが生成されるため、finalクラスやfinalメソッドに付与するとエラーになる。"),
        ("@RequestScoped", "jakarta.enterprise.context\n(javax.enterprise.context)", "〇 認識される\n(Bean定義)", "通常スコープ (Normal Scope)\n1回のHTTPリクエスト中のみ生存", "Webリクエストごとのコンテキスト情報を安全に保持・破棄するため。", "非同期スレッドやバッチスレッドから参照するとContextNotActiveExceptionが発生する。"),
        ("@SessionScoped", "jakarta.enterprise.context\n(javax.enterprise.context)", "〇 認識される\n(Bean定義)", "通常スコープ (Normal Scope)\nHTTPセッション単位で生存", "ログインユーザーの状態やカート情報を管理するため。", "Serializable を実装していないとデプロイ時に検証エラー（DefinitionException）になる。"),
        ("@ConversationScoped", "jakarta.enterprise.context\n(javax.enterprise.context)", "〇 認識される\n(Bean定義)", "通常スコープ (Normal Scope)\n複数画面にまたがる対話単位", "JSF等のウィザード画面で特定の期間だけ状態を保つため。", "CDI 4.0 Liteでは仕様から除外されているため、モダンフレームワークでは非推奨。"),
        ("@Dependent", "jakarta.enterprise.context\n(javax.enterprise.context)", "〇 認識される\n(Bean定義)", "疑似スコープ (Pseudo Scope)\n注入先のオブジェクトの寿命に完全従属", "CDIのデフォルトスコープ。注入されるたびに新しいインスタンスが生成される。", "明示的に @Dependent と書けば annotated モードでもBeanになるが、省略すると annotated モードではBeanにならない！"),
        ("@Stereotype 付きアノテーション\n(例: @Model)", "jakarta.enterprise.inject.Model\n等", "〇 認識される\n(Bean定義)", "メタアノテーションで定義されたスコープに従う（@Modelは@RequestScoped+@Named）", "共通の設定セット（Web層用モデル等）をまとめて付与する設計パターンのため。", "自作ステレオタイプを作る場合、@Stereotypeだけでなくスコープも含めて定義する必要がある。"),
        ("@Inject", "jakarta.inject.Inject\n(javax.inject.Inject)", "× 認識されない！\n(Bean定義ではない)", "なし（単なるインジェクションポイント指定子）", "【重要】@Injectは「依存を注入してくれ」という受動的な要求であり、クラス自身の身元・スコープを定義するものではない！", "【最頻出トラブル】クラス内に @Inject を書いたからBeanとしてスキャンされると誤解し、クラススコープを忘れて脱落する。"),
        ("@Named (単体)", "jakarta.inject.Named\n(javax.inject.Named)", "× 認識されない！\n(スコープ未指定時)", "なし（EL式/テンプレートから参照するための名前付け）", "@NamedはEL式から名前解決するための識別子に過ぎず、CDIのライフサイクルスコープを定義しないため。", "JSF等で @Named だけ書いてスコープを忘れると、annotated モードではBeanとして認識されない！"),
        ("@Singleton", "jakarta.inject.Singleton\nvs jakarta.ejb.Singleton", "△ 要注意\n(疑似スコープだが実装依存あり)", "擬似スコープ（プロキシを作らないシングルトン）", "JSR-330標準のSingletonだが、CDI仕様上の通常スコープではないためプロキシが生成されない。", "EJBの @Singleton と混同しやすい。CDI標準では @ApplicationScoped の使用が強く推奨される。")
    ]

    for row_idx, r in enumerate(data_tab3_sec3, start=19):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws3.row_dimensions[row_idx].height = 46
        for col_idx, val in enumerate(r, start=1):
            cell = ws3.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2, 3] else align_left_top

    col_widths_3 = {1: 22, 2: 24, 3: 20, 4: 28, 5: 36, 6: 38}
    for col_idx, w in col_widths_3.items():
        ws3.column_dimensions[get_column_letter(col_idx)].width = w

    # =========================================================================
    # TAB 4: 04_beans.xml設定完全仕様
    # =========================================================================
    ws4 = wb.create_sheet(title="04_beans.xml設定完全仕様")
    apply_sheet_base(ws4, "A6")

    ws4.merge_cells("A1:F1")
    ws4["A1"] = "【完全リファレンス】beans.xml の構文・スキーマ定義・全タグ・全属性・配置場所"
    ws4["A1"].font = font_sheet_title
    ws4["A1"].fill = fill_sheet_title
    ws4["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws4.row_dimensions[1].height = 40

    ws4.merge_cells("A2:F2")
    ws4["A2"] = "技術仕様完全解説：CDI 1.1〜4.0までのXSDスキーマ宣言、ルート要素の属性、<scan>タグによるクラス除外・条件付きスキャン、<trim/>タグ、およびJAR/WARにおける物理配置パスの完全仕様です。"
    ws4["A2"].font = font_sheet_subtitle
    ws4["A2"].fill = fill_sheet_subtitle
    ws4["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws4.row_dimensions[2].height = 28

    # Section 1
    ws4.merge_cells("A4:F4")
    ws4["A4"] = "第1章：CDIバージョン別 XSDスキーマ宣言完全コード一覧"
    ws4["A4"].font = font_section_header
    ws4["A4"].fill = fill_section_header
    ws4["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws4.row_dimensions[4].height = 28

    headers_tab4_sec1 = ["CDIバージョン", "対応仕様", "ルート要素構文 (完全なXML宣言サンプル)", "デフォルトの bean-discovery-mode", "名前空間 (Namespace) URI", "特記事項"]
    for col_idx, h in enumerate(headers_tab4_sec1, start=1):
        cell = ws4.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws4.row_dimensions[5].height = 26

    data_tab4_sec1 = [
        ("CDI 4.0\n(最新・推奨)", "Jakarta EE 10 / 11",
         '<beans xmlns="https://jakarta.ee/xml/ns/jakartaee"\n       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n       xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee\n                           https://jakarta.ee/xml/ns/jakartaee/beans_4_0.xsd"\n       version="4.0" bean-discovery-mode="annotated">\n</beans>',
         "annotated\n(空ファイルでもannotated)", "https://jakarta.ee/xml/ns/jakartaee", "version=\"4.0\" を指定。CDI Lite環境（Quarkus 3等）ではこれが標準。"),

        ("CDI 3.0", "Jakarta EE 9",
         '<beans xmlns="https://jakarta.ee/xml/ns/jakartaee"\n       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n       xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee\n                           https://jakarta.ee/xml/ns/jakartaee/beans_3_0.xsd"\n       version="3.0" bean-discovery-mode="annotated">\n</beans>',
         "all\n(未指定時はall動作)", "https://jakarta.ee/xml/ns/jakartaee", "パッケージ名がjakartaになった過渡期のバージョン。"),

        ("CDI 2.0", "Java EE 8",
         '<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"\n       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n       xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee\n                           http://xmlns.jcp.org/xml/ns/javaee/beans_2_0.xsd"\n       version="2.0" bean-discovery-mode="annotated">\n</beans>',
         "all\n(未指定時はall動作)", "http://xmlns.jcp.org/xml/ns/javaee", "<trim/> 要素が利用可能になったバージョン。"),

        ("CDI 1.1 / 1.2", "Java EE 7",
         '<beans xmlns="http://xmlns.jcp.org/xml/ns/javaee"\n       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n       xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee\n                           http://xmlns.jcp.org/xml/ns/javaee/beans_1_1.xsd"\n       version="1.1" bean-discovery-mode="annotated">\n</beans>',
         "all\n(未指定時はall動作)", "http://xmlns.jcp.org/xml/ns/javaee", "bean-discovery-mode 属性が初めて導入された歴史的バージョン。")
    ]

    for row_idx, r in enumerate(data_tab4_sec1, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws4.row_dimensions[row_idx].height = 70
        for col_idx, val in enumerate(r, start=1):
            cell = ws4.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_code if col_idx == 3 else font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2, 4] else align_left_top

    # Section 2: beans.xml Element Reference
    ws4.merge_cells("A11:F11")
    ws4["A11"] = "第2章：beans.xml 全要素・属性・子タグ完全リファレンス"
    ws4["A11"].font = font_section_header
    ws4["A11"].fill = fill_section_header
    ws4["A11"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws4.row_dimensions[11].height = 28

    headers_tab4_sec2 = ["タグ名 / 属性名", "親要素", "指定可能な値 (設定値の候補)", "デフォルト値", "機能と動作内容の解説", "具体的なXML記述例"]
    for col_idx, h in enumerate(headers_tab4_sec2, start=1):
        cell = ws4.cell(row=12, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws4.row_dimensions[12].height = 26

    data_tab4_sec2 = [
        ("bean-discovery-mode\n(属性)", "<beans>", "\"annotated\" | \"all\" | \"none\"", "CDI 4.0: annotated\nCDI 1.1-3.0: all",
         "アーカイブ内のクラスをどのような基準でCDI Beanとして登録・スキャンするかを制御する最重要属性。",
         '<beans bean-discovery-mode="annotated">'),

        ("version\n(属性)", "<beans>", "\"4.0\" | \"3.0\" | \"2.0\" | \"1.1\"", "スキーマ依存",
         "使用するCDI仕様のバージョン番号。スキーマ検証に使用される。",
         '<beans version="4.0">'),

        ("<trim/>\n(空要素タグ)", "<beans>", "タグの有無のみ", "なし（トリム無効）",
         "【CDI 2.0+】Beanアーカイブ内の未使用の型（他のBeanからインジェクションされない型）をコンテナのメタデータから除外しメモリを節約する。",
         '<beans ...>\n  <trim/>\n</beans>'),

        ("<scan>\n(子要素タグ)", "<beans>", "<exclude> タグを含む", "スキャン除外なし",
         "クラスパススキャン時のフィルタリングルールを定義する。特定のパッケージやテスト用クラスをCDI管理外に追放できる。",
         '<beans ...>\n  <scan>\n    <exclude name="com.example.mock.**"/>\n  </scan>\n</beans>'),

        ("<exclude>\n(子要素タグ)", "<scan>", "name 属性（Ant形式ワイルドカード：* または **）", "必須",
         "スキャン対象から除外する完全修飾クラス名またはパッケージパターンを指定する。末尾の .* は同一パッケージ、.** はサブパッケージ含む。",
         '<exclude name="com.example.experimental.**"/>'),

        ("<if-class-available>\n(条件タグ)", "<exclude>", "name 属性（クラスの完全修飾名）", "なし",
         "【条件付き除外】指定されたクラスがクラスローダー上でロード可能な場合に限り、対象を除外する。",
         '<exclude name="com.example.LegacyService">\n  <if-class-available name="org.dummy.Mock"/>\n</exclude>'),

        ("<if-system-property>\n(条件タグ)", "<exclude>", "name 属性（プロパティ名）、value 属性（期待値）", "なし",
         "【条件付き除外】JVMシステムプロパティ（-Dkey=val）が一致する場合に限り、対象を除外する。環境別の切替に有用。",
         '<exclude name="com.example.DevOnlyService">\n  <if-system-property name="env" value="prod"/>\n</exclude>'),

        ("<interceptors>\n(子要素タグ)", "<beans>", "<class> タグのリスト", "なし",
         "インターセプタの適用優先順位をXMLで明示的に宣言する（通常は @Priority アノテーションを使用するが、XMLでも指定可能）。",
         '<interceptors>\n  <class>com.example.LoggingInterceptor</class>\n</interceptors>'),

        ("<alternatives>\n(子要素タグ)", "<beans>", "<class> または <stereotype> のリスト", "なし",
         "有効化する代替Bean（モックやテスト用実装）を宣言する。複数実装から特定の実装を選択する際に使用。",
         '<alternatives>\n  <class>com.example.MockPaymentService</class>\n</alternatives>')
    ]

    for row_idx, r in enumerate(data_tab4_sec2, start=13):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws4.row_dimensions[row_idx].height = 48
        for col_idx, val in enumerate(r, start=1):
            cell = ws4.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_code if col_idx in [1, 6] else font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2, 4] else align_left_top

    # Section 3: Physical File Placement
    ws4.merge_cells("A23:F23")
    ws4["A23"] = "第3章：アーカイブ種別・ビルドツール別 beans.xml 物理配置パス完全仕様"
    ws4["A23"].font = font_section_header
    ws4["A23"].fill = fill_section_header
    ws4["A23"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws4.row_dimensions[23].height = 28

    headers_tab4_sec3 = ["アーカイブ種別", "ビルドツール (Maven / Gradle) ソースパス", "パッケージング後の成果物内パス", "コンテナの検出ロジック", "誤った配置例 (事故の元)", "検出成否"]
    for col_idx, h in enumerate(headers_tab4_sec3, start=1):
        cell = ws4.cell(row=24, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws4.row_dimensions[24].height = 26

    data_tab4_sec3 = [
        ("標準ライブラリJAR\n(Java SE / 共通部品)", "src/main/resources/META-INF/beans.xml", "my-library.jar!\n/META-INF/beans.xml",
         "ClassLoader.getResources(\"META-INF/beans.xml\") で検出。", "src/main/java/beans.xml\n(クラスパス直下に置く誤り)", "〇 正常検出"),

        ("Webアプリケーション\n(WARプロジェクト)", "src/main/webapp/WEB-INF/beans.xml\nまたは\nsrc/main/resources/META-INF/beans.xml", "my-app.war!\n/WEB-INF/beans.xml\nまたは\n/WEB-INF/classes/META-INF/beans.xml",
         "ServletContext.getResource(\"/WEB-INF/beans.xml\") および WEB-INF/classes 内のMETA-INFを検出。", "src/main/webapp/META-INF/beans.xml\n(WAR直下のMETA-INFに置く誤り！)", "〇 正常検出"),

        ("WAR内の同梱ライブラリ\n(WEB-INF/lib/*.jar)", "各ライブラリプロジェクトの\nsrc/main/resources/META-INF/beans.xml", "my-app.war!\n/WEB-INF/lib/sub-module.jar!\n/META-INF/beans.xml",
         "WEB-INF/lib内の各JARファイルを個別のアーカイブとして検査し、その中のMETA-INF/beans.xmlを検出。", "親WARのWEB-INF/beans.xmlがあるからlib内のJARも自動で対象になると誤認する誤り！", "〇 JAR個別に必要"),

        ("エンタープライズEAR\n(EARプロジェクト)", "src/main/application/META-INF/beans.xml", "my-app.ear!\n/lib/shared.jar!/META-INF/beans.xml",
         "EAR直下はBeanアーカイブにならない。EARの /lib ディレクトリ内の共有JARごとにbeans.xmlを検査。", "EAR直下のMETA-INFにbeans.xmlを置けばEAR内全モジュールに効くと誤認する誤り！", "× EAR直下は無効")
    ]

    for row_idx, r in enumerate(data_tab4_sec3, start=25):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws4.row_dimensions[row_idx].height = 46
        for col_idx, val in enumerate(r, start=1):
            cell = ws4.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_code if col_idx in [2, 3, 5] else font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 6] else align_left_top

    col_widths_4 = {1: 22, 2: 32, 3: 34, 4: 26, 5: 36, 6: 38}
    for col_idx, w in col_widths_4.items():
        ws4.column_dimensions[get_column_letter(col_idx)].width = w

    # =========================================================================
    # TAB 5: 05_失敗パターンと解決レシピ
    # =========================================================================
    ws5 = wb.create_sheet(title="05_失敗パターンと解決レシピ")
    apply_sheet_base(ws5, "A6")

    ws5.merge_cells("A1:G1")
    ws5["A1"] = "【実務トラブルシューティング】@Inject が効かない5大失敗パターンと解決コード集"
    ws5["A1"].font = font_sheet_title
    ws5["A1"].fill = fill_sheet_title
    ws5["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws5.row_dimensions[1].height = 40

    ws5.merge_cells("A2:G2")
    ws5["A2"] = "現場の即戦力ナレッジ：開発現場で「@Injectを書いたのに動かない！」と頭を抱える原因の99%を網羅。各パターンの症状、発生メカニズム、NGコード、OK修正コード、および設定ファイルの完全な処方箋を提示します。"
    ws5["A2"].font = font_sheet_subtitle
    ws5["A2"].fill = fill_sheet_subtitle
    ws5["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws5.row_dimensions[2].height = 28

    # Section 1
    ws5.merge_cells("A4:G4")
    ws5["A4"] = "第1章：@Inject が効かない5大失敗パターンの徹底解剖"
    ws5["A4"].font = font_section_header
    ws5["A4"].fill = fill_section_header
    ws5["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws5.row_dimensions[4].height = 28

    headers_tab5_sec1 = ["パターン番号", "トラブルの名称", "発生する症状・エラーメッセージ", "根本原因 (Why?)", "NGコード例 (失敗)", "OKコード例 (解決)", "必要なbeans.xml設定 / 処方箋"]
    for col_idx, h in enumerate(headers_tab5_sec1, start=1):
        cell = ws5.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws5.row_dimensions[5].height = 26

    data_tab5_sec1 = [
        ("パターン 1", "【親がCDI管理外の罠】\n呼び出し元を new してしまった",
         "実行時例外：\nNullPointerException\n（@Injectされたフィールドが null のままメソッド呼び出しして即死）",
         "CDIコンテナは『自身がインスタンス化したオブジェクト』に対してのみインジェクションを行う。プログラマが new MyController() と書くと、JVM標準のコンストラクタが走るだけでCDIは一切介入できない。",
         "// NG: 呼び出し元を手動new\nMyService service = new MyService();\nservice.execute(); // 内部の@Injectがnull！",
         "// OK: 呼び出し元自身も@Inject\n@Inject\nprivate MyService service;\n// またはCDI.current()で取得\nMyService s = CDI.current().select(MyService.class).get();",
         "親クラスの所属するアーカイブに beans.xml が存在し、親クラス自身にも @ApplicationScoped 等を付与する。"),

        ("パターン 2", "【外部ライブラリ非アーカイブの罠】\n注入先JARにbeans.xmlがない",
         "デプロイ/起動時例外：\nWELD-001408: Unsatisfied dependencies for type TargetService with qualifiers @Default at injection point...",
         "注入しようとしている TargetService クラスがサードパーティ製JARの中にあり、そのJARに beans.xml がなく、かつBean定義アノテーションも付いていないため非Beanアーカイブとして無視された。",
         "// NG: 非Beanアーカイブ内のクラスを直接Inject\n@Inject\nprivate ThirdPartyClient client;",
         "// OK: @Producesプロデューサメソッドを自作\n@ApplicationScoped\npublic class Factory {\n  @Produces\n  public ThirdPartyClient produce() {\n    return new ThirdPartyClient();\n  }\n}",
         "外部JARの内部は変更できないため、自作アプリ側に @Produces メソッドを作成してコンテナにBeanとして登録する。"),

        ("パターン 3", "【暗黙的アーカイブのスコープ省略の罠】\nクラスにスコープがない",
         "デプロイ/起動時例外：\nUnsatisfiedResolutionException\n（クラスに@Injectはあるのに見つからないとエラー）",
         "JARに beans.xml がない（暗黙的アーカイブ）。暗黙的アーカイブでは『Bean定義アノテーション』を持つクラスしかスキャンされない。クラスに @Inject はあってもクラスレベルの @ApplicationScoped や @Dependent が無いためスキップされた。",
         "// NG: クラスにスコープがない\npublic class OrderProcessor {\n  @Inject private PaymentDao dao;\n}",
         "// OK: 明示的にスコープを付与する\n@ApplicationScoped\npublic class OrderProcessor {\n  @Inject private PaymentDao dao;\n}",
         "クラス宣言に必ず @ApplicationScoped や @Dependent を付与する。またはモジュールに beans.xml (bean-discovery-mode=\"all\") を配置する。"),

        ("パターン 4", "【CDI 4.0移行の罠】\n空のbeans.xmlの解釈が激変した",
         "アップグレード直後の全滅：\nJakarta EE 10に移行した途端、既存の多くのBeanで UnsatisfiedResolutionException が発生！",
         "CDI 1.1〜3.0では空のbeans.xmlは bean-discovery-mode=\"all\" だったが、CDI 4.0から \"annotated\" がデフォルトになった。スコープアノテーションを省略していた過去のレガシーBeanが一斉に対象外になった。",
         "<!-- NG: CDI 4.0で空のbeans.xml -->\n<beans ...>\n  <!-- 属性省略 -> annotated扱い！ -->\n</beans>",
         "<!-- OK: 明示的にallを指定して復旧 -->\n<beans ... bean-discovery-mode=\"all\">\n</beans>\n<!-- 推奨: 全Beanにスコープを付与する -->",
         "beans.xml で bean-discovery-mode=\"all\" を明示的に指定するか、または移行作業として全クラスに @ApplicationScoped などを付与する。"),

        ("パターン 5", "【ファイルパス・配置場所ミスの罠】\nリソースフォルダの階層違い",
         "実行時例外または起動時例外：\n全くCDIが機能せず、beans.xmlが存在しない時と同一の挙動を示す。",
         "Maven/Gradleで beans.xml の配置場所を誤っている。例：WARなのに WEB-INF ではなく直下の META-INF に置いた、あるいは src/main/java の直下に置いてパッケージング時に欠落した。",
         "// NG配置例 (Maven WAR):\nsrc/main/webapp/META-INF/beans.xml\nsrc/main/resources/beans.xml",
         "// OK配置例 (Maven WAR):\nsrc/main/webapp/WEB-INF/beans.xml\n// OK配置例 (JARライブラリ):\nsrc/main/resources/META-INF/beans.xml",
         "ビルド後の war/jar ファイルを zip 解凍し、正しい位置に beans.xml が存在するか物理構造を目視確認する。")
    ]

    for row_idx, r in enumerate(data_tab5_sec1, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws5.row_dimensions[row_idx].height = 68
        for col_idx, val in enumerate(r, start=1):
            cell = ws5.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_code if col_idx in [5, 6] else font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx == 1 else align_left_top

    # Section 2: Flowchart Check Table
    ws5.merge_cells("A12:G12")
    ws5["A12"] = "第2章：@Inject 不発トラブル診断フローチャート（チェックリスト）"
    ws5["A12"].font = font_section_header
    ws5["A12"].fill = fill_section_header
    ws5["A12"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws5.row_dimensions[12].height = 28

    headers_tab5_sec2 = ["ステップ", "チェック項目 (自己問答)", "「YES」の場合の進路", "「NO」の場合の原因と対処アクション", "該当パターン", "確認コマンド・手法", "重要度"]
    for col_idx, h in enumerate(headers_tab5_sec2, start=1):
        cell = ws5.cell(row=13, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws5.row_dimensions[13].height = 26

    flow_data = [
        ("Step 1", "呼び出し元のオブジェクト自身は、CDIコンテナ（@Inject）から取得していますか？", "Step 2 へ進む。", "【即死原因】new しています！呼び出し元も @Inject するか CDI.current() を使用してください。", "パターン 1", "呼び出し箇所のJavaコードを grep 検索", "最重要 (★5)"),
        ("Step 2", "ビルド成果物（JAR/WAR）の中に、beans.xml が正しいパスで同梱されていますか？", "Step 3 へ進む。", "【未検出】配置パスの誤りです。jar tf myapp.war | grep beans.xml で配置を確認してください。", "パターン 5", "jar tf <ファイル名> コマンドで物理確認", "最重要 (★5)"),
        ("Step 3", "注入対象のクラス自身に、@ApplicationScoped などのスコープが付与されていますか？", "Step 4 へ進む。", "【暗黙除外】クラスにスコープがありません！@ApplicationScoped などをクラスに付与してください。", "パターン 3", "クラス宣言の先頭アノテーションを目視確認", "重要 (★4)"),
        ("Step 4", "CDI 4.0 (Jakarta EE 10) を使用しており、beans.xml の bean-discovery-mode を省略していませんか？", "bean-discovery-mode を明記しているのでOK。Step 5 へ。", "【4.0の罠】省略すると annotated になります！all を明記するか全クラスにスコープを付与してください。", "パターン 4", "beans.xml の bean-discovery-mode 属性を確認", "重要 (★4)"),
        ("Step 5", "注入対象はサードパーティ製の外部ライブラリ（JAR）ですか？", "外部ライブラリです。対処アクションを実行。", "自作クラスです。型パラメータやQualifier（@Default等）の不一致を疑ってください。", "パターン 2", "@Produces ファクトリメソッドを作成してBean化", "普通 (★3)")
    ]

    for row_idx, r in enumerate(flow_data, start=14):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws5.row_dimensions[row_idx].height = 42
        for col_idx, val in enumerate(r, start=1):
            cell = ws5.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 5, 7] else align_left_top

    col_widths_5 = {1: 14, 2: 24, 3: 28, 4: 34, 5: 38, 6: 38, 7: 36}
    for col_idx, w in col_widths_5.items():
        ws5.column_dimensions[get_column_letter(col_idx)].width = w

    # =========================================================================
    # TAB 6: 06_内部動作原理と処理フロー
    # =========================================================================
    ws6 = wb.create_sheet(title="06_内部動作原理と処理フロー")
    apply_sheet_base(ws6, "A6")

    ws6.merge_cells("A1:G1")
    ws6["A1"] = "【深堀り動作原理】CDIコンテナの起動・型解決・プロキシ生成・注入の全6フェーズ詳細"
    ws6["A1"].font = font_sheet_title
    ws6["A1"].fill = fill_sheet_title
    ws6["A1"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws6.row_dimensions[1].height = 40

    ws6.merge_cells("A2:G2")
    ws6["A2"] = "内部アーキテクチャの全容：CDIコンテナ（Weld / SmallRye ArC / OpenWebBeans）が起動時にどのようにクラスを探索し、型安全解決（Typesafe Resolution）を行い、クライアントプロキシを生成してフィールドに注入するかの全フローを解剖します。"
    ws6["A2"].font = font_sheet_subtitle
    ws6["A2"].fill = fill_sheet_subtitle
    ws6["A2"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws6.row_dimensions[2].height = 28

    # Section 1
    ws6.merge_cells("A4:G4")
    ws6["A4"] = "第1章：CDIコンテナ起動時の内部処理 6大フェーズ完全解説"
    ws6["A4"].font = font_section_header
    ws6["A4"].fill = fill_section_header
    ws6["A4"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws6.row_dimensions[4].height = 28

    headers_tab6_sec1 = ["フェーズ番号", "フェーズ名 (正式名称)", "実行トリガー・契機", "コンテナの内部処理詳細", "関連する仕様・インターフェース", "このフェーズで発生する障害・エラー", "Beanアーカイブ非存在時の挙動"]
    for col_idx, h in enumerate(headers_tab6_sec1, start=1):
        cell = ws6.cell(row=5, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    ws6.row_dimensions[5].height = 26

    data_tab6_sec1 = [
        ("Phase 1", "アーカイブ識別・分類\n(Archive Identification)", "アプリケーションのデプロイ開始直後",
         "クラスパス上の全JARおよびWEB-INFディレクトリを走査。beans.xmlの有無とbean-discovery-mode属性を読み取り、「明示的アーカイブ」「暗黙的アーカイブ」「非Beanアーカイブ」に3分割する。",
         "CDI Spec Chapter 12\nDeployment", "beans.xml のXML構文エラー（SAXParseException）など。",
         "【スキップ発生】\nBeanアーカイブでないと判定されたJARは、これ以降のPhase 2〜6から完全に除外される！"),

        ("Phase 2", "型検出・バイトコード走査\n(Type Discovery)", "アーカイブ分類完了後",
         "各アーカイブ内の .class バイトコード（JandexインデックスやASM）を走査。<scan>除外ルールを適用後、mode=\"all\"なら全クラス、mode=\"annotated\"ならBean定義アノテーション付きクラスを抽出する。",
         "ProcessAnnotatedType\n(拡張イベント)", "クラスロード失敗（NoClassDefFoundError、ClassNotFoundException）。",
         "クラスが存在していても、スキャン対象リストに一切追加されず無視される。"),

        ("Phase 3", "Beanメタデータ構築\n(Bean Definition Building)", "型検出完了後",
         "抽出された各クラスから、スコープ、型、修飾子（Qualifiers）、@Inject フィールド、@Produces メソッド、@PostConstruct などを解析し、BeanManager に Bean<?> と InjectionPoint の登録オブジェクトを作成する。",
         "ProcessBeanAttributes\nProcessInjectionPoint", "スコープ定義矛盾（DefinitionException）、Finalクラスへの通常スコープ付与エラー。",
         "BeanManager に該当クラスのメタデータが1件も登録されない。"),

        ("Phase 4", "型安全解決・整合性検証\n(Typesafe Resolution & Validation)", "全Bean登録完了後",
         "コンテナ内のすべての InjectionPoint（注入要求）に対して、合致する Bean<?> を型と修飾子でマッチング。マッチ数が0件なら Unsatisfied、2件以上で優先順位がなければ Ambiguous として起動を中断する（Fail-Fast原則）。",
         "BeanManager.getBeans()\nTypesafe Resolution Algorithm", "UnsatisfiedResolutionException\nAmbiguousResolutionException\n（起動が即座にクラッシュ）",
         "注入先が存在しないため、UnsatisfiedResolutionException が発生する！"),

        ("Phase 5", "クライアントプロキシ生成\n(Client Proxy Generation)", "検証成功後、実行準備時",
         "通常スコープ（@ApplicationScoped, @RequestScoped 等）のBeanに対し、ByteBuddyやJavassistを用いて動的サブクラス（クライアントプロキシ）のバイトコードを生成する。",
         "ClientProxy\nContextual Storage", "UnproxyableBeanException\n（privateコンストラクタのみ、finalクラス/メソッドの存在）",
         "Beanが存在しないためプロキシ生成すら行われない。"),

        ("Phase 6", "コンテキスト結合・値注入\n(Contextual Injection & Execution)", "リクエスト受付時 / 呼出時",
         "オブジェクトが必要になった時、コンテキストからインスタンスを取得（なければ生成）。フィールドのリフレクションまたは生成済みアクセサを介して、プロキシまたは実インスタンスをフィールドに代入する。",
         "CreationalContext\nContext.get()", "実行時例外（ビジネスロジック中のエラー、DB接続失敗等）。",
         "手動で new されたオブジェクトの場合、このフェーズが一切トリガーされず null のままとなる！")
    ]

    for row_idx, r in enumerate(data_tab6_sec1, start=6):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws6.row_dimensions[row_idx].height = 64
        for col_idx, val in enumerate(r, start=1):
            cell = ws6.cell(row=row_idx, column=col_idx, value=val)
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2] else align_left_top

    # Section 2: Client Proxy deep dive
    ws6.merge_cells("A13:G13")
    ws6["A13"] = "第2章：クライアントプロキシ（Client Proxy）の動作イメージとスコープの仕組み"
    ws6["A13"].font = font_section_header
    ws6["A13"].fill = fill_section_header
    ws6["A13"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws6.row_dimensions[13].height = 28

    headers_tab6_sec2 = ["比較項目", "通常スコープ (Normal Scopes: @ApplicationScoped, @RequestScoped)", "疑似スコープ (Pseudo Scopes: @Dependent, @Singleton)", "なぜこのような差があるのか？", "インジェクション時の実体"]
    ws6.merge_cells("E14:G14")
    for col_idx, h in enumerate(headers_tab6_sec2[:4], start=1):
        cell = ws6.cell(row=14, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    c_last = ws6.cell(row=14, column=5, value=headers_tab6_sec2[4])
    c_last.font = font_table_header
    c_last.fill = fill_table_header
    c_last.alignment = align_center
    c_last.border = border_header
    for ck in [6, 7]:
        ws6.cell(row=14, column=ck).border = border_header
    ws6.row_dimensions[14].height = 26

    proxy_data = [
        ("プロキシの有無", "【プロキシを生成する】\n注入されるのは本物ではなく、本物の皮をかぶった薄い代理人（Proxy）。", "【プロキシなし】\n実際のインスタンスが直接フィールドに注入される。",
         "リクエストスコープのように『スレッドごとにインスタンスが異なる』オブジェクトを、シングルトン（ApplicationScoped）な親に安全に注入するため。", "動的生成されたサブクラス（例: MyService$Proxy$WeldClientProxy）"),

        ("メソッド呼び出し時の挙動", "プロキシが現在のスレッド・コンテキスト（ThreadLocal）から本物のインスタンスを取得し、処理を本物に委譲（デリゲート）する。", "直接インスタンスのメソッドが直接実行される。",
         "スレッドが切り替わっても、プロキシ経由であれば常に『そのスレッドの現在のRequest』の実体に届くようにするため。", "コンテキストストレージ（Contextual Store）へのルックアップが発生"),

        ("破棄タイミング\n(ライフサイクル)", "コンテキスト終了時（リクエスト終了時、アプリ停止時）に @PreDestroy が呼ばれて安全に破棄される。", "親オブジェクトがGCされるとき、またはCreationalContextが解放されたとき。",
         "リソースリーク（メモリリーク）を防止し、ステートフルなコンポーネントを安全にクリーンアップするため。", "コンテナがライフサイクルを厳密に管理")
    ]

    for row_idx, r in enumerate(proxy_data, start=15):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws6.row_dimensions[row_idx].height = 56
        for col_idx in range(1, 5):
            cell = ws6.cell(row=row_idx, column=col_idx, value=r[col_idx-1])
            cell.font = font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx == 1 else align_left_top
        
        ws6.merge_cells(start_row=row_idx, start_column=5, end_row=row_idx, end_column=7)
        cell_m = ws6.cell(row=row_idx, column=5, value=r[4])
        cell_m.font = font_data
        cell_m.fill = fill_curr
        cell_m.alignment = align_left_top
        for ck in range(5, 8):
            ws6.cell(row=row_idx, column=ck).border = border_cell

    # Section 3: Debug commands
    ws6.merge_cells("A19:G19")
    ws6["A19"] = "第3章：実務でのCDIデバッグログ有効化コマンド一覧（サーバー・フレームワーク別）"
    ws6["A19"].font = font_section_header
    ws6["A19"].fill = fill_section_header
    ws6["A19"].alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws6.row_dimensions[19].height = 28

    headers_tab6_sec3 = ["フレームワーク / APサーバー", "CDI実装", "設定ファイル / コマンド", "設定内容 (Log Category / Level)", "得られるデバッグ情報", "使い所のヒント"]
    ws6.merge_cells("F20:G20")
    for col_idx, h in enumerate(headers_tab6_sec3[:5], start=1):
        cell = ws6.cell(row=20, column=col_idx, value=h)
        cell.font = font_table_header
        cell.fill = fill_table_header
        cell.alignment = align_center
        cell.border = border_header
    c_last = ws6.cell(row=20, column=6, value=headers_tab6_sec3[5])
    c_last.font = font_table_header
    c_last.fill = fill_table_header
    c_last.alignment = align_center
    c_last.border = border_header
    ws6.cell(row=20, column=7).border = border_header
    ws6.row_dimensions[20].height = 26

    cmd_data = [
        ("WildFly / JBoss EAP", "Weld (JBoss)", "jboss-cli.sh / jboss-cli.bat",
         "/subsystem=logging/logger=org.jboss.weld:add(level=DEBUG)\n/subsystem=logging/logger=org.jboss.weld.Bootstrap:write-attribute(name=level,value=TRACE)",
         "どのJARがBeanアーカイブとして認識されたか、各クラスがどのスコープで登録されたかがログに1行ずつ出力される。", "起動時にBeanが見つからない場合の最強の調査手段。"),

        ("Quarkus", "SmallRye ArC", "application.properties",
         "quarkus.log.category.\"io.quarkus.arc\".level=DEBUG\nquarkus.arc.unremovable-types=com.example.**",
         "ビルド時（コンパイル時）にどのクラスがBeanとして検出され、どのクラスが未使用として削除されたかが全てわかる。", "CDI 4.0 Liteで未使用Beanが消去（Removal）される問題を追跡する際に必須。"),

        ("Open Liberty / WebSphere", "Apache OpenWebBeans", "server.xml",
         "<logging traceSpecification=\"org.apache.webbeans.*=all=enabled:com.ibm.ws.cdi.*=all=enabled\"/>",
         "アーカイブスキャンの詳細、インジェクションポイントの解決過程がtrace.logに出力される。", "IBM Liberty環境でのデプロイエラー解析に即座に活用可能。"),

        ("スタンドアロン Java SE", "Weld SE", "logging.properties",
         "org.jboss.weld.level = FINEST\nhandlers = java.util.logging.ConsoleHandler",
         "コンテナ初期化からシャットダウンまでの全イベントログを標準出力に出力。", "バッチ処理やCLIアプリでの単体デバッグに最適。")
    ]

    for row_idx, r in enumerate(cmd_data, start=21):
        fill_curr = fill_row_white if row_idx % 2 == 0 else fill_row_zebra
        ws6.row_dimensions[row_idx].height = 48
        for col_idx in range(1, 6):
            cell = ws6.cell(row=row_idx, column=col_idx, value=r[col_idx-1])
            cell.font = font_code if col_idx in [3, 4] else font_data
            cell.fill = fill_curr
            cell.border = border_cell
            cell.alignment = align_center_top if col_idx in [1, 2] else align_left_top
        
        ws6.merge_cells(start_row=row_idx, start_column=6, end_row=row_idx, end_column=7)
        cell_m = ws6.cell(row=row_idx, column=6, value=r[5])
        cell_m.font = font_data
        cell_m.fill = fill_curr
        cell_m.alignment = align_left_top
        for ck in range(6, 8):
            ws6.cell(row=row_idx, column=ck).border = border_cell

    col_widths_6 = {1: 14, 2: 24, 3: 28, 4: 36, 5: 34, 6: 32, 7: 32}
    for col_idx, w in col_widths_6.items():
        ws6.column_dimensions[get_column_letter(col_idx)].width = w

    # Save workbook
    output_filename = "CDI_BeanArchive_Complete_Specification.xlsx"
    wb.save(output_filename)
    print(f"Successfully generated {output_filename} with Meiryo UI & Monotone Palette")

if __name__ == "__main__":
    build_workbook()
