#!/usr/bin/env python3
"""Build the news-image-20261121 v1 front page (1024x1024, JPEG).

Build-time only (Pillow). Classic newspaper front page for Saturday
21 November 2026: masthead + stats strip + region tabs + 3 lead
features + 10 medium stories + world map with pins + 23 briefs +
DATE CHECK strip + footer. All illustrations are flat-vector images
generated fresh in-session (assets/), one per featured story.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")

PAGE_W, PAGE_H = 1024, 1024
PAPER = (247, 241, 222)
INK = (28, 28, 28)
RED = (168, 35, 42)
NAVY = (30, 58, 95)
DARK = (22, 40, 63)
TEAL = (42, 122, 122)
OCHRE = (181, 126, 30)
GREEN = (46, 125, 50)
PURPLE = (106, 76, 147)
GREY = (107, 101, 88)
LINE = (216, 207, 184)

FDIR = "/usr/share/fonts/truetype/liberation"


def get_font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FDIR, name), size)
    except OSError:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)


SERIF = "LiberationSerif-Regular.ttf"
SERIF_B = "LiberationSerif-Bold.ttf"
SERIF_I = "LiberationSerif-Italic.ttf"
SANS = "LiberationSans-Regular.ttf"
SANS_B = "LiberationSans-Bold.ttf"


def wrap_text(draw, text, font, width):
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def tracked_left(draw, x, y, text, font, fill, step=2):
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + step
    return x


def fit_crop(im, tw, th):
    sw, sh = im.size
    if sw / sh > tw / th:
        nw = int(sh * tw / th)
        x0 = (sw - nw) // 2
        im = im.crop((x0, 0, x0 + nw, sh))
    else:
        nh = int(sw * th / tw)
        y0 = (sh - nh) // 2
        im = im.crop((0, y0, sw, y0 + nh))
    return im.resize((tw, th), Image.LANCZOS)


def load_img(name):
    return Image.open(os.path.join(ASSETS, name)).convert("RGB")


# ------------------------------------------------------------------ content
STATS = [
    ("400+", "drones & missiles in Kyiv barrage"),
    ("-3.7%", "S&P 500 enters correction"),
    ("300,000+", "evacuated ahead of Cyclone Akvan"),
    ("$3.79bn", "GTA VI first-day sales"),
    ("7/58", "Starc's Ashes spell in Perth"),
    ("-14%", "Nvidia in a single day"),
]

REGIONS = [
    ("EUROPE", 9, NAVY),
    ("AMERICAS", 10, RED),
    ("ASIA-PACIFIC", 5, TEAL),
    ("MIDEAST", 4, OCHRE),
    ("AFRICA", 3, GREEN),
    ("OCEANIA", 3, PURPLE),
    ("WORLD", 2, (85, 85, 85)),
]

LEADS = [
    dict(img="f01.jpg", tag_l="400+ DRONES \u00b7 100+ MISSILES",
         tag_r="\u22658 KILLED",
         kick="01 \u00b7 KYIV, UKRAINE \u00b7 WAR",
         head="Russia launches war's biggest barrage at Kyiv",
         cap="Overnight waves hit energy sites and bridges; fires burn "
             "in three districts; power cut across the capital. "
             "(Reuters, Kyiv Post)"),
    dict(img="f02.jpg", tag_l="S&P -3.7% \u00b7 DOW -950 PTS",
         tag_r="WORST WEEK SINCE 2020",
         kick="02 \u00b7 NEW YORK \u00b7 MARKETS",
         head="S&P and Dow enter correction as AI rout deepens",
         cap="Nasdaq -5.3% erases its 2026 gains; Nvidia -14% as its "
             "CEO is ousted; fear gauge spikes to 40. (AP, WSJ)"),
    dict(img="f03.jpg", tag_l="UN CLIMATE SUMMIT \u00b7 ANTALYA",
         tag_r="DRAFT DROPS 'FOSSIL FUELS'",
         kick="03 \u00b7 ANTALYA, T\u00dcRKIYE \u00b7 CLIMATE",
         head="COP31 into overtime as fossil-fuel talks deadlock",
         cap="Closing draft omits any fossil-fuel phase-out; Panama "
             "demands a global oil cap; finance gap unresolved. "
             "(Reuters, UN News)"),
]

MEDIUM = [
    dict(img="f04.jpg", badge="300,000 EVACUATED", bc=TEAL,
         kick="04 \u00b7 ODISHA, INDIA \u00b7 CYCLONE",
         head="Cyclone Akvan makes landfall in eastern India",
         cap="Storm crosses near Gopalpur; 300,000+ evacuated. (IMD)"),
    dict(img="f05.jpg", badge="'PROVOCATION'", bc=RED,
         kick="05 \u00b7 POLAND \u00b7 WAR",
         head="Russian missiles crash in Poland",
         cap="Two missiles and a drone down in the south-east. (ToI)"),
    dict(img="f06.jpg", badge="DIPLOMAT EXPELLED", bc=NAVY,
         kick="06 \u00b7 COPENHAGEN \u00b7 ESPIONAGE",
         head="Denmark expels Russian diplomat over plot to kill rapper",
         cap="Moscow recruited a gang to kill rapper Kyivstoner. "
             "(Al Jazeera)"),
    dict(img="f07.jpg", badge="THREE-WAY SUMMIT", bc=NAVY,
         kick="07 \u00b7 WASHINGTON \u00b7 DIPLOMACY",
         head="Trump calls Putin 'friend' at talks with Xi",
         cap="Summit discusses Korea and a Ukraine peace push. "
             "(Korea Times)"),
    dict(img="f08.jpg", badge="$3.79BN DAY ONE", bc=PURPLE,
         kick="08 \u00b7 LOS ANGELES \u00b7 GAMES",
         head="GTA VI takes $3.79bn on day one",
         cap="Biggest entertainment debut ever, past every film and "
             "game launch on record. (TradingView)"),
    dict(img="f09.jpg", badge="-14% \u00b7 CEO OUT", bc=RED,
         kick="09 \u00b7 SANTA CLARA \u00b7 CHIPS",
         head="Nvidia craters as CEO is ousted and SEC probes books",
         cap="Shares -14% in a day, -23% in a week. (WSJ, IBD)"),
    dict(img="f10.jpg", badge="7/58 \u00b7 ASHES", bc=TEAL,
         kick="10 \u00b7 PERTH \u00b7 CRICKET",
         head="Starc 7/58 wrecks England for 172 in Perth",
         cap="Stokes hits back 5/23; Australia 123/9 at stumps. "
             "(Glance)"),
    dict(img="f11.jpg", badge="BELOW $59K", bc=OCHRE,
         kick="11 \u00b7 CRYPTO \u00b7 MARKETS",
         head="Bitcoin below $59,000 in seventh weekly fall",
         cap="Longest losing run since 2022; Strategy -30%. "
             "(TradingView)"),
    dict(img="f12.jpg", badge="MILITIA STRONGHOLD", bc=NAVY,
         kick="12 \u00b7 IRAQ \u00b7 SECURITY",
         head="Iraqi troops move into Iran-backed militia stronghold",
         cap="Forces deploy in Jurf al-Nasr, held a decade. "
             "(NBC News)"),
    dict(img="f13.jpg", badge="22,000 CHILDREN", bc=RED,
         kick="13 \u00b7 GAZA \u00b7 WAR",
         head="Gaza: 22,000 children killed, ministry says",
         cap="Ministry toll passes 22,000 children. (News wires)"),
]

BRIEFS = [
    (14, "EU", "\u20ac1bn military aid for Ukraine", "Reuters"),
    (15, "POLAND", "11 nations drill for postwar Ukraine mission", "AP"),
    (16, "FRANCE", "Seeks UN Security Council meeting on Kyiv strikes", "AFP"),
    (17, "RUTTE", "NATO chief flies to Warsaw", "Reuters"),
    (18, "KREMLIN", "Refuses NATO-like guarantees for Ukraine", "Daily Finland"),
    (19, "PANAMA", "Calls for global oil cap at COP31", "Reuters"),
    (20, "HOUTHIS", "Saudi coalition downs Houthi missiles", "Shipwr3ck"),
    (21, "CYBER", "JPMorgan, Visa, Mastercard hit in vendor attack", "JagranJosh"),
    (22, "ASIA MARKETS", "Nikkei -5.06%, Kospi -5.21%, Taiex -5.65%", "Mazala"),
    (23, "ANTHROPIC", "-8.5% on day two after record IPO", "Dimsum Daily"),
    (24, "ZSCALER", "+20% on CrowdStrike takeover talks", "TradingView"),
    (25, "VIX", "Fear gauge spikes to 40", "IBD"),
    (26, "CRICKET", "Gill out, Pant to lead India in 2nd Test", "Glance"),
    (27, "WPL", "277 players for 73 spots at 27 Nov auction", "Glance"),
    (28, "BOXING", "India women win seven golds, 20-medal sweep", "Glance"),
    (29, "RUGBY", "Wales host Australia in Cardiff", "Planet Rugby"),
    (30, "HAITI", "Two Salvadorans killed handling explosives", "umsicht"),
    (31, "T20I", "Australia v England, 1st T20I at the MCG", "Cricinfo"),
    (32, "MOROCCO", "Record fifth in FIFA rankings", "iintroo"),
    (33, "PAN CUP", "South Sudan Women v Ethiopia Women, Sat 21 Nov", "Instagram"),
    (34, "RABADA", "South Africa pacer ruled out of 2nd Test", "Glance"),
    (35, "RUBICON", "Ukraine strikes elite Russian drone base in Kursk", "erudite"),
    (36, "ETHICS DAY", "70 countries mark Ethics Day 2026", "umsicht"),
]

# pin number -> (x, y) on the page; map image sits at x 24..344, y 712..872.
# Europe/Mideast + US east coast spread by eye so no two pins touch.
PINS = {
    1: (200, 748), 2: (88, 760), 3: (198, 772), 4: (257, 786),
    5: (178, 748), 6: (172, 736), 7: (96, 772), 8: (100, 786),
    9: (64, 766), 10: (295, 819), 12: (216, 770), 13: (206, 780),
}
PIN_KEY = [
    "1 Kyiv", "2 New York", "3 Antalya", "4 Odisha", "5 Poland",
    "6 Copenhagen", "7 Washington", "8 Miami", "9 Santa Clara",
    "10 Perth", "12 Iraq", "13 Gaza",
]

DATE_CHECK = ("First reported Friday 20 Nov or earlier, so NOT shown as "
              "Saturday's news: Trump\u2013Xi\u2013Putin Shenzhen summit "
              "itself \u00b7 ICJ Myanmar Rohingya verdict \u00b7 Houthi "
              "missile hits Riyadh tower \u00b7 US Senate rejects Iran "
              "war-powers bill \u00b7 BepiColombo reaches Mercury \u00b7 "
              "Phillips 118 vs India \u00b7 Russell fastest in wet Las "
              "Vegas GP practice \u00b7 Japan CPI 2.3% \u00b7 Microsoft "
              "explains 12 Nov outage.")

# ------------------------------------------------------------------ drawing
page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
dr = ImageDraw.Draw(page)
M = 16
CW = PAGE_W - 2 * M

# masthead
tracked_left(dr, M, 10, "THE WORLD IN ONE DAY", get_font(SANS_B, 13), RED, 2)
dr.text((PAGE_W - M, 12), "SATURDAY'S NEWS \u00b7 ONE PAGE \u00b7 36 STORIES \u00b7 7 REGIONS",
        font=get_font(SANS_B, 10), fill=INK, anchor="ra")
dr.text((PAGE_W // 2, 26), "Saturday 21 November 2026",
        font=get_font(SERIF_B, 58), fill=INK, anchor="ma")
dr.text((PAGE_W // 2, 92),
        "Kyiv's biggest barrage \u00b7 Wall Street enters correction \u00b7 "
        "COP31 deadlocked into overtime \u00b7 Cyclone Akvan",
        font=get_font(SERIF_I, 15), fill=RED, anchor="ma")
dr.rectangle([M, 112, PAGE_W - M, 114], fill=INK)
dr.rectangle([M, 117, PAGE_W - M, 117], fill=INK)

# stats strip
cell = CW / 6
for i, (num, cap) in enumerate(STATS):
    cx = M + cell * i + cell / 2
    dr.text((cx, 122), num, font=get_font(SANS_B, 23), fill=RED, anchor="ma")
    for j, line in enumerate(wrap_text(dr, cap, get_font(SANS, 9), cell - 16)):
        dr.text((cx, 149 + j * 11), line, font=get_font(SANS, 9),
                fill=INK, anchor="ma")
    if i:
        x = M + cell * i
        dr.line([x, 124, x, 168], fill=LINE, width=1)
dr.line([M, 174, PAGE_W - M, 174], fill=LINE, width=1)

# region tabs
x = M
ytab = 180
for name, count, color in REGIONS:
    label = f"{name} {count}"
    f = get_font(SANS_B, 10)
    tw = dr.textlength(label, font=f)
    dr.rounded_rectangle([x, ytab, x + tw + 14, ytab + 20], radius=9,
                         fill=color)
    dr.text((x + 7, ytab + 10), label, font=f, fill=(255, 255, 255),
            anchor="lm")
    x += tw + 14 + 6
dr.text((PAGE_W - M, ytab + 10), "ALL STORIES: SAT 21 NOV 2026, ANY TIME ZONE",
        font=get_font(SANS_B, 9), fill=GREY, anchor="rm")

# 3 lead features
col_w, gap = 324, 10
for i, f in enumerate(LEADS):
    x0 = M + i * (col_w + gap)
    im = fit_crop(load_img(f["img"]), col_w, 108)
    page.paste(im, (x0, 208))
    dr.rectangle([x0, 208 + 108 - 18, x0 + col_w, 208 + 108], fill=DARK)
    dr.text((x0 + 6, 208 + 108 - 9), f["tag_l"], font=get_font(SANS_B, 9),
            fill=(255, 255, 255), anchor="lm")
    dr.text((x0 + col_w - 6, 208 + 108 - 9), f["tag_r"],
            font=get_font(SANS_B, 9), fill=(255, 255, 255), anchor="rm")
    dr.text((x0, 320), f["kick"], font=get_font(SANS_B, 11), fill=RED)
    for j, line in enumerate(wrap_text(dr, f["head"], get_font(SERIF_B, 16),
                                       col_w)[:2]):
        dr.text((x0, 334 + j * 18), line, font=get_font(SERIF_B, 16),
                fill=INK)
    for j, line in enumerate(wrap_text(dr, f["cap"], get_font(SANS, 10),
                                       col_w)[:3]):
        dr.text((x0, 372 + j * 12), line, font=get_font(SANS, 10), fill=INK)

# 10 medium stories, 2 rows of 5
med_w = (CW - 4 * 8) // 5
for r in range(2):
    y0 = 415 + r * 134
    for c in range(5):
        f = MEDIUM[r * 5 + c]
        x0 = M + c * (med_w + 8)
        im = fit_crop(load_img(f["img"]), med_w, 60)
        page.paste(im, (x0, y0))
        bf = get_font(SANS_B, 8)
        bw = dr.textlength(f["badge"], font=bf)
        dr.rectangle([x0, y0, x0 + bw + 10, y0 + 13], fill=f["bc"])
        dr.text((x0 + 5, y0 + 6), f["badge"], font=bf,
                fill=(255, 255, 255), anchor="lm")
        dr.text((x0, y0 + 64), f["kick"], font=get_font(SANS_B, 9), fill=RED)
        for j, line in enumerate(wrap_text(dr, f["head"], get_font(SERIF_B, 12),
                                           med_w)[:2]):
            dr.text((x0, y0 + 76 + j * 14), line, font=get_font(SERIF_B, 12),
                    fill=INK)
        for j, line in enumerate(wrap_text(dr, f["cap"], get_font(SANS, 9),
                                           med_w)[:2]):
            dr.text((x0, y0 + 106 + j * 11), line, font=get_font(SANS, 9),
                    fill=INK)

# map + briefs headers
dr.text((M, 684), "WHERE IT HAPPENED", font=get_font(SANS_B, 12), fill=INK)
dr.text((362, 684), "ALSO ON SATURDAY 21 NOVEMBER \u2014 23 MORE STORIES",
        font=get_font(SANS_B, 13), fill=INK)
dr.text((PAGE_W - M, 686), "World Briefs (14\u201336)", font=get_font(SANS, 9),
        fill=GREY, anchor="ra")
dr.line([362, 702, PAGE_W - M, 702], fill=LINE, width=1)

# map panel
dr.rectangle([M, 706, 352, 956], fill=DARK)
m = fit_crop(load_img("map.jpg"), 320, 160)
page.paste(m, (24, 712))
for n, (px, py) in PINS.items():
    dr.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED,
               outline=(255, 255, 255), width=1)
    dr.text((px, py), str(n), font=get_font(SANS_B, 8),
            fill=(255, 255, 255), anchor="mm")
kf = get_font(SANS, 9)
for i, label in enumerate(PIN_KEY):
    col = 0 if i < 6 else 1
    row = i if i < 6 else i - 6
    dr.text((24 + col * 164, 880 + row * 11), label, font=kf,
            fill=(240, 236, 220))

# briefs, two columns
bf = get_font(SANS, 9)
bbf = get_font(SANS_B, 9)
for i, (n, loc, text, src) in enumerate(BRIEFS):
    col = 0 if i < 12 else 1
    row = i if i < 12 else i - 12
    x0 = 362 + col * 330
    y0 = 708 + row * 20
    num = f"{n} "
    dr.text((x0, y0), num, font=bbf, fill=RED)
    nx = x0 + dr.textlength(num, font=bbf)
    head = f"{loc} \u2014 "
    dr.text((nx, y0), head, font=bbf, fill=INK)
    tx = nx + dr.textlength(head, font=bbf)
    dr.text((tx, y0), f"{text} ({src})", font=bf, fill=INK)

# DATE CHECK strip
dr.rectangle([M, 962, PAGE_W - M, 992], fill=(242, 221, 210))
dr.rectangle([M, 962, 104, 992], fill=RED)
dr.text((60, 977), "DATE CHECK", font=get_font(SANS_B, 11),
        fill=(255, 255, 255), anchor="mm")
for j, line in enumerate(wrap_text(dr, DATE_CHECK, get_font(SANS, 9),
                                   PAGE_W - M - 112 - 8)[:2]):
    dr.text((112, 966 + j * 12), line, font=get_font(SANS, 9), fill=INK)

# footer
dr.text((M, 999), "Every story here happened, or was first reported, on "
        "Saturday 21 November 2026 in at least one time zone.",
        font=get_font(SANS, 8), fill=GREY)
dr.text((PAGE_W - M, 999), "36 STORIES \u00b7 7 REGIONS \u00b7 SOURCES: Reuters, "
        "AP, AFP, BBC, IMD, UN News, Al Jazeera, WSJ, IBD, ICC, NBC, ToI.",
        font=get_font(SANS_B, 8), fill=GREY, anchor="ra")

out = os.path.join(BASE, "entry.png")
page.save(out, "JPEG", quality=88, optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
