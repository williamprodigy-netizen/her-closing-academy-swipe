#!/usr/bin/env python3
"""Build the Her Closing Academy swipe site.

ONE SITE PER COMPETITOR. Ava Mistruzzi runs two funnels off the same Framer
site and both live here:

  F047 (captured 2 Aug 2026) — the VSL funnel, /u3 -> /ft3 -> /pc.
       Their opt-in resisted automation, so it was captured downstream. The
       pre-call confirmation gate on /pc is still the best show-rate idea in
       the swipe file.

  F121 (captured 6 Aug 2026) — the LIVE WEBINAR funnel, /w -> /wc -> /replay
       -> /application. Found from her Instagram link in bio. The replay is
       ungated, so the entire 2h14m pitch was captured without registering.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/AVA_MISTRUZZI_Swipe")          # F121
OLD = os.path.expanduser("~/Downloads/Swipes/HER_CLOSING_ACADEMY_Swipe")  # F047


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True,
            timeout=60).stdout.strip()))
    except Exception:
        return 0


NOTES = {
    "masterclass_replay.mp4":
        "The full live masterclass, pulled off the ungated /replay page. "
        "ConverteAI HLS, 2h14m, 20,213 words.",
    "confirmation_indoc_video.mp4":
        "The indoctrination video on /wc. Three minutes, and it is where the "
        "Sales Career Fast Pass show-rate mechanic is set up.",
}


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        n = os.path.basename(p)
        mb = os.path.getsize(p) / 1e6
        rows.append((n, _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     NOTES.get(n, "")))
    for p in sorted(glob.glob(os.path.join(OLD, "Recording/*.mp4"))):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     "F047 — student interview from the VSL funnel. One-to-one "
                     "conversation, not a produced testimonial."))
    return rows


CONFIG = {
    "SITE": "Her Closing Academy — Ava Mistruzzi",
    "CREATOR": "Ava Mistruzzi",
    "ADS_KEY": "her_closing_academy",
    "FUNNEL_IDS": ["F047", "F121"],
    "CAPTURED": "2 & 6 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/AVA_MISTRUZZI_Swipe",
    "BLURB": "Remote high-ticket <i>closing</i> sold to women &mdash; the closest ICP "
             "match to UGC World in this file, with the product swapped: she sells "
             "getting <b>placed on someone else&rsquo;s offer</b>, we sell creating "
             "content. Two funnels off one site. The three things worth stealing are "
             "the <b>Fast Pass</b> show-rate mechanic, a bonus stack that pays for a "
             "<b>booking</b> rather than a sale, and a deliberate on-mic refusal to "
             "state the price.",

    "PAGES": [
        ("index.html", "Overview"),
        ("board.html", "The board"),
        ("analysis.html", "Analysis"),
        ("slides.html", "Masterclass slides"),
        ("decks.html", "Decks"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("ICP", "Women, 9–5 escape"),
        ("Promise", "$10K–$30K/mo, 90 days"),
        ("Funnels live", "2 (VSL + webinar)"),
        ("Masterclass", "2h 14m 19s"),
        ("Words transcribed", "20,213"),
        ("Deck slides", "78"),
        ("Bonus stack", "$9,979"),
        ("Price", "never stated"),
    ],

    "OFFER": [
        ("Product", "Her Closing Academy — remote high-ticket closing training + "
                    "placement, for women"),
        ("Mechanism named", "&ldquo;Soft selling to build a soft life&rdquo;"),
        ("Hook (webinar)", "&ldquo;Learn How Women Are Choosing a <i>Soft Life</i> And "
                           "Becoming Financially Free in 90 Days With Remote Sales&rdquo;"),
        ("Hook (replay)", "&ldquo;The Fastest Way Women Are Making $10K&ndash;$30K/Month "
                          "Without a Degree, Boss, or Office&rdquo;"),
        ("Objection stripped on a slide", "not manipulation &middot; not pushy &middot; "
                                          "not a 9&ndash;5 grind &middot; not capped "
                                          "&middot; not just for extroverts &middot; not "
                                          "cold calling &middot; <b>not MLM</b> &middot; "
                                          "not burnout"),
        ("Opt-in (webinar)", "Name, email, country, <b>phone required</b> — modal, "
                             "posts to a Zapier catch hook"),
        ("Delivery", "12-week accelerator &rarr; 20&ndash;30 mock calls &rarr; placement "
                     "at week 8 &rarr; job portal (200+ roles listed in one week)"),
        ("Path", "IG bio &rarr; /w &rarr; WebinarJam &rarr; /wc &rarr; live class &rarr; "
                 "/replay &rarr; /application &rarr; Calendly"),
        ("Price", "<b>Never stated.</b> Not on a page, not on any of 227 extracted frames, not in "
                  "20,213 transcribed words. Refused on-mic at 1:47:18"),
        ("Proof", "Six full YouTube case studies on the confirmation page, 12&ndash;26 "
                  "min each. <b>Zero proof on the registration page.</b>"),
    ],

    "FINDINGS": [
        ("The Fast Pass — the cheapest show-rate mechanic in the file",
         "The confirmation video promises a free &ldquo;Sales Career Fast Pass&rdquo; guide "
         "gated behind three conditions: <b>reply to the email</b> with the words "
         "&ldquo;I will be at the event&rdquo;, <b>show up on time on a laptop</b>, and "
         "<b>stay to the end</b> — &ldquo;that is how the fast pass activates and it gets "
         "sent to you right after.&rdquo; One PDF buys a reply (which is also a "
         "deliverability signal), a micro-commitment, an on-time attendance and a "
         "stay-to-the-end. Cost to her: zero."),
        ("The bonus stack pays for a booking, not a sale",
         "At 09:14 she promises <b>$5,000</b> in bonuses for staying to the end. At "
         "1:20:35 it becomes <b>$10,000</b> — and the condition quietly changes from "
         "<i>stay</i> to <b>book today</b>. The slide totals seven bonuses at "
         "<b>$9,979</b> and says &ldquo;yours free when you book today.&rdquo; Every "
         "bonus dollar is spent buying a calendar slot."),
        ("She refuses the price on purpose, out loud, and frames the refusal as service",
         "Asked directly in the Q&amp;A at 1:47:18: <i>&ldquo;we really have investment "
         "ranges that fit anyone&rsquo;s budget… I would be doing you a huge disservice "
         "if we just had a checkout link right on here, because it&rsquo;s not like that, "
         "it has to be customized and personalized to you.&rdquo;</i> Same play as 1 "
         "Percent Academy. Two competitors, same market shape, both hand the number to "
         "a human on the phone."),
        ("Proof is withheld from the registration page and dumped after the opt-in",
         "The reg page has no testimonial, no logo, no number — just a countdown and a "
         "seat bar. The confirmation page then carries six full case-study interviews, "
         "12&ndash;26 minutes each. Two of the six were published the day before capture, "
         "so the proof block is maintained continuously. The bet: proof does not buy the "
         "opt-in, it buys the attendance."),
        ("The whole class is a typed-commitment machine",
         "Chat prompts are built into the deck roughly every ten minutes — <i>type "
         "&ldquo;I RELATE&rdquo;</i>, <i>&ldquo;I AM BREAKING FREE TODAY&rdquo;</i>, "
         "<i>&ldquo;I AM CLAIMING MY SOFT LIFE NOW&rdquo;</i> — and at the close "
         "<b>&ldquo;Let&rsquo;s congratulate the ladies who have booked tonight! Type "
         "&lsquo;I&rsquo;M IN&rsquo; in the chat&rdquo;</b>, which converts other "
         "people&rsquo;s bookings into live social proof."),
        ("The DIY teardown is the offer",
         "One slide does the maths on doing it alone: 10 DMs a day, 2% reply, 50 companies "
         "needed to land one role, therefore <b>2,500 DMs and 12,500 minutes of unpaid "
         "work</b>. The placement portal is then screen-shared with 200+ live roles at "
         "$6K&ndash;$20K/mo on-target. The arithmetic <i>is</i> the pitch."),
        ("The pre-call gate on the older VSL funnel — still the best single idea here",
         "F047 serves <b>&ldquo;Your Call Is Booked, But Not Yet Confirmed&rdquo;</b> "
         "after booking, telling the lead to watch a video <b>&ldquo;to make sure we "
         "don&rsquo;t cancel your call&rdquo;</b>, with the next step <b>locked for "
         "2:00</b>. Commitment declared unfinished, loss framed on something just gained, "
         "and the video cannot be skipped."),
        ("Scarcity is asserted three different ways and never reconciled",
         "&ldquo;I have <b>18 spots</b> and you only have the next 30 minutes&rdquo; "
         "(1:26:26). Twenty minutes later, &ldquo;my tech guy just messaged me, we only "
         "have <b>two spots left</b>&rdquo; (2:01:57). Then &ldquo;we have <b>113 "
         "women</b> left, half of our ladies are gone&rdquo; (2:06:53). Spot count, "
         "timer and room count all move independently."),
        ("Build hygiene is poor — read this before copying anything",
         "The replay page still runs a dead script watching for an <b>iClosed</b> iframe "
         "and redirecting to <code>flipland.info/pc</code> or <code>/dq497</code>, with "
         "the embed URL <code>app.iclosed.io/e/mentorme/land-flipping-strategy-call</code> "
         "— a land-flipping funnel&rsquo;s booking widget left inside the template. The "
         "replay headline links to <code>preview--forged-site-analytics.lovable.app</code>. "
         "Her Calendly slug is literally <code>…-clone-2</code>. The funnel converts "
         "anyway, which is the actual lesson."),
    ],

    "FUNNEL": [
        ("F121 · Registration", "learn.herclosingacademy.com/w?el=ig-bio",
         '<span class="tag good">the entry</span> From her Instagram bio. Countdown, '
         '&ldquo;LIMITED SPOTS AVAILABLE&rdquo; seat bar, two identical CTAs, zero proof. '
         'The <code>?el=</code> parameter is a Hyros source label, not a UTM.'),
        ("F121 · Registration variant B", "learn.herclosingacademy.com/w2",
         "Same promise on a second slug. Countdown reads 00:00:00, so it is parked."),
        ("F121 · Opt-in modal", "(modal on /w)",
         '<span class="tag bad">phone required</span> Name, email, country, phone. Posts '
         'to <code>hooks.zapier.com/hooks/catch/21266060/4olnuab/</code>, fires the Meta '
         'pixel itself, then redirects to /wc. She owns the lead in Zapier before '
         'WebinarJam sees it.'),
        ("F121 · Confirmation", "learn.herclosingacademy.com/wc",
         '<span class="tag good">the Fast Pass</span> 2m59s indoctrination video, '
         'add-to-calendar shown as a screenshot of the real WebinarJam mail, then six '
         'full YouTube case studies.'),
        ("F121 · The class", "event.webinarjam.com",
         "Thursday 8:00PM EST. Mail from ops@herclosingacademy via em.webinarjam.net. "
         "The confirmation screenshot she posts is dated March 19 2026 — same asset, "
         "rolling dates."),
        ("F121 · Replay", "learn.herclosingacademy.com/replay",
         '<span class="tag good">ungated</span> No password, no email wall, no expiry. '
         'The full 2h14m pitch, served to anyone with the URL.'),
        ("F121 · Application", "learn.herclosingacademy.com/application",
         '&ldquo;Your Application Is Approved!&rdquo; — with no application on the page, '
         'just an inline Calendly (<code>close-her-academy/her-closing-academy-clone-2</code>). '
         'Approval is asserted, never earned. Hyros fires <code>tag=!application</code>.'),
        ("F047 · Opt-in", "learn.herclosingacademy.com/u3",
         '<span class="tag bad">resisted automation</span> Four fields. Captured, not '
         'registered.'),
        ("F047 · Free training", "learn.herclosingacademy.com/ft3",
         "The training page behind the opt-in."),
        ("F047 · Pre-call gate", "learn.herclosingacademy.com/pc",
         '<span class="tag good">the mechanic</span> &ldquo;Booked, but not yet '
         'confirmed&rdquo; &middot; threat to cancel &middot; next step locked 2:00.'),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The masterclass (F121)",
         [os.path.join(PKG, "Transcript/transcript.md"),
          os.path.join(PKG, "Transcript/indoc_transcript.md")]),
        ("Student interviews (F047)",
         sorted(glob.glob(os.path.join(OLD, "Transcript/*.md")))),
    ],

    "SLIDE_PAGES": [
        ("Masterclass slides", "slides.html", "Screenshots", "web_",
         "Every materially different frame from the 2h14m masterclass, talking-head "
         "frames stripped."),
    ],

    "DECKS": [
        ("Her Closing Academy — Ava Mistruzzi Masterclass", 78,
         "https://docs.google.com/presentation/d/1xzt5YoNmD8GewTxRMNuUc621vGKBGvRqZ8VzfEz5KI0/edit"),
    ],

    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="note"><b>Two funnels, one operator, one avatar that is ours.</b> Ava Mistruzzi
sells women the same escape we do — out of the 9-to-5, remote, no degree, no following —
and then hands them a different vehicle. She places them on someone else&rsquo;s offer as a
closer; we teach them to create. Every mechanic below is transferable because the buyer is
the same buyer.</div>

<h2 class="sec">1. The Fast Pass — steal this first</h2>
<p>Three minutes of video on the confirmation page do the work that our setters currently do
by hand. The lead is told to <b>reply to the confirmation email</b> with the exact words
&ldquo;I will be at the event&rdquo;, then to <b>show up on time from a laptop</b> and
<b>stay to the end</b>, and only then does the free guide arrive.</p>
<div class="tablewrap"><table>
<tr><th>Condition</th><th>What it actually buys</th></tr>
<tr><td>Reply with &ldquo;I will be at the event&rdquo;</td><td>A written micro-commitment, plus a reply to the sending domain — which is a deliverability signal for every mail after it.</td></tr>
<tr><td>Show up on time, on a laptop</td><td>Kills the phone-in half-watch. Desktop attendees stay longer and can click the booking link.</td></tr>
<tr><td>Stay to the end</td><td>The pitch is at the end. This is a stay-rate lever disguised as a gift.</td></tr>
<tr><td>Delivered after, by email</td><td>Costs one PDF and one automation. No discount, no bonus, no spend.</td></tr>
</table></div>
<p style="margin-top:12px">Our show rate is the metric we have spent the year on, and our
current answer is follow-up volume. This is the opposite approach: make the lead do a small
piece of work while intent is hot, and make skipping it forfeit something.</p>

<h2 class="sec">2. The stack pays for a booking, not a sale</h2>
<p>The bonus promise escalates mid-class and swaps its own condition.</p>
<div class="tablewrap"><table>
<tr><th>Timestamp</th><th>What is said</th><th>Condition</th></tr>
<tr><td>00:09:14</td><td>&ldquo;$5,000 worth of exclusive bonuses I normally reserve for my paid students&rdquo;</td><td>stay to the end</td></tr>
<tr><td>01:20:35</td><td>&ldquo;not just 5,000, but <b>$10,000</b> worth of free gifts&rdquo;</td><td><b>book today</b></td></tr>
<tr><td>01:25:30 (slide)</td><td>Seven bonuses totalling <b>$9,979</b></td><td>&ldquo;yours free when you book today&rdquo;</td></tr>
</table></div>
<p style="margin-top:12px">The whole stack is spent on a calendar slot. Nothing is sold in
the room. Worth weighing against how we currently spend bonus value at the point of sale.</p>

<h2 class="sec">3. The price is refused, on purpose, on mic</h2>
<p>At <b>01:47:18</b> she reads the question out and declines it: <i>&ldquo;we really have
investment ranges that fit anyone&rsquo;s budget… I would be doing you a huge disservice if
we just had a checkout link right on here, because it&rsquo;s not like that, it has to be
customized and personalized to you.&rdquo;</i> The refusal is framed as care, and it is
immediately followed by &ldquo;that&rsquo;s exactly why you book your call.&rdquo;</p>
<p>No figure appears anywhere: not on a page, not on any of the 227 extracted slides, not in
20,213 transcribed words. <b>1 Percent Academy does the identical thing.</b> Two independent
competitors selling women a high-ticket escape both blackout the number until a human is on
the line — that convergence is the signal, not the coincidence.</p>

<h2 class="sec">4. Proof is deliberately absent from the page that needs the click</h2>
<p>The registration page carries no testimonial, no logo and no number. The confirmation
page — <i>after</i> the lead is captured — carries six full case-study interviews of
12&ndash;26 minutes. Two of the six were published the day before we captured, so this block
is actively maintained.</p>
<div class="tablewrap"><table>
<tr><th>Case study</th><th>Length</th><th>Published</th><th>Claim in the copy</th></tr>
<tr><td>Kari</td><td>12:55</td><td>16 Apr 2026</td><td>$18k in one week; scaling to 30–50k profit months; was $32k in debt</td></tr>
<tr><td>Alexa</td><td>17:35</td><td>23 Mar 2026</td><td>Consistent 10k months; saved 100k; down payment on a home</td></tr>
<tr><td>Phoenix</td><td>14:29</td><td>7 Mar 2026</td><td>Broke college girl to net 30k months</td></tr>
<tr><td>Lara</td><td>26:34</td><td>24 Feb 2026</td><td>$10k in her second month, while in law school</td></tr>
<tr><td>Sarah</td><td>24:25</td><td>5 Aug 2026</td><td>New mom, $20k/mo working 5 hours a day</td></tr>
<tr><td>Courtney</td><td>18:48</td><td>5 Aug 2026</td><td>Extra $10k/mo without quitting the 9–5</td></tr>
</table></div>
<p style="margin-top:12px">Read the bet: proof does not buy the opt-in, proof buys the
attendance. Our reg pages do the opposite.</p>

<h2 class="sec">5. Her numbers, as she states them</h2>
<div class="tablewrap"><table>
<tr><th>Claim</th><th>Where</th></tr>
<tr><td>Closed $2.5M–$2.6M in one year</td><td>indoc video 01:41 · slides, repeated</td></tr>
<tr><td>$360,000 in commissions in a year (slide says $359,000)</td><td>00:33:48 · slide</td></tr>
<tr><td>#1 closer out of 100 reps, beat the next best by more than double</td><td>slide &ldquo;My journey&rdquo;</td></tr>
<tr><td>Took over 4,000 sales calls</td><td>01:03:17</td></tr>
<tr><td>Mentored 500+ women zero to 10K months</td><td>00:11:41</td></tr>
<tr><td>Placement portal: 200+ roles in one week, $6K–$20K/mo on-target</td><td>01:08:07, screen-shared</td></tr>
<tr><td>Placement at week 8, after 20–30 mock calls</td><td>01:07:21, 01:52:55</td></tr>
</table></div>
<p style="margin-top:12px">Stated, not verified. The commission figure differs by $1,000
between what she says and what her own slide shows.</p>

<h2 class="sec">Stack fingerprint</h2>
<div class="tablewrap"><table>
<tr><th>Layer</th><th>What she runs</th></tr>
<tr><td>Pages</td><td>Framer (single site, siteId d06982fb0f1a…)</td></tr>
<tr><td>Registration</td><td>Custom Framer form component &rarr; Zapier catch hook</td></tr>
<tr><td>Webinar</td><td>WebinarJam (em.webinarjam.net)</td></tr>
<tr><td>Replay / indoc video</td><td>ConverteAI smartplayer, HLS</td></tr>
<tr><td>Booking</td><td>Calendly (<code>close-her-academy</code>)</td></tr>
<tr><td>Course platform</td><td>Whop — <code>js.whop.com/static/checkout</code> loads on every page, and the portal screen-share is a Whop curriculum view</td></tr>
<tr><td>Attribution</td><td><b>Hyros</b>, account 214166, first-party subdomain <code>t.herclosingacademy.com</code>, source labels via <code>?el=</code></td></tr>
<tr><td>Analytics</td><td>Meta pixel 677603008333760 · GA4 G-LBWCM41JZX · Humblytics dd6e2ec</td></tr>
<tr><td>UTMs</td><td>None. Hyros source labels do the job instead.</td></tr>
</table></div>

<h2 class="sec">Read carefully</h2>
<p><b>Not registered, and it did not matter.</b> The webinar opt-in requires a phone number
and we hold no research number, so the funnel was never opted into. The replay page is
completely ungated, which is where the full 2h14m pitch came from.</p>
<p><b>Every price on this page was read off a slide, not off the transcript.</b> Whisper
renders each $1,497 as &ldquo;14.97&rdquo;, so a text search for the formatted number returns
nothing on a transcript that states it four times.</p>
<p><b>Paid traffic is unresolved.</b> She carries a Meta pixel and Hyros source labels, which
is consistent with running ads, but no Her Closing Academy ads appear in the Gethookd library
and the Meta Ad Library refused our requests. Do not claim she is organic-only.</p>
<p><b>Ignore two artefacts in her bundles.</b> The iClosed / flipland.info block on /replay is
dead template code from a land-flipping funnel, and the Calendly URL in
<code>shared.mjs</code> belongs to the Inovat Framer template author. Neither is hers. Also,
the capture engine reports &ldquo;Typeform&rdquo; on three pages — there is no Typeform, it
is a Framer layer named <code>typeform</code>.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
