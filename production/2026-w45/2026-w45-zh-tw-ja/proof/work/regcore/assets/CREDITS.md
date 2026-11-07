# Image credits — Lucerna Weekly W45 Traditional Chinese core (VOL.2)

Only Public Domain / CC0 images are used. Credit lines are taken from the
Wikimedia Commons API Artist field as recorded in the W43 verified set,
except P4, which was replaced during the post-proof fix round (see below).

| File | Page | Subject | Author (Commons API Artist field) | License | Commons page |
|---|---|---|---|---|---|
| harbour.jpg | P1 | Victoria Harbour / ICC skyline, file photo | Wilfredor | CC0 | W43 verified set (no file-page URL recorded in this build) |
| rain.jpg | P2 | Rain on a blue umbrella, file photo | CorraleH | CC0 | W43 verified set (no file-page URL recorded in this build) |
| baseball.jpg | P4 | Washington baseball team, 1908 (Bain News Service glass negative), file photo of an old baseball team | Bain News Service | Public domain | https://commons.wikimedia.org/wiki/File:Washington_team,_Washington_AL_(baseball)_LCCN2014680242.jpg |
| pumpkin.jpg | P5 | Carved jack-o'-lantern, file photo | Benjamin Balazs | CC0 | W43 verified set (no file-page URL recorded in this build) |

## P4 fix record (post-proof, 2026-10-27)

The pre-fix P4 file was a batter mid-swing photo (1280×1920, SHA-256
6222d8c91c439b2f0a734b6d8aaaea5100fcd5c801d092e3b05e05f1885f89a2) inherited
from the W43 set, credited "unknown author — Public domain (Wikimedia
Commons)". No Commons file name or file-page URL for that file exists in
the W43 kit, in this build, or anywhere else in the workspace (SHA-256
search across all build copies), and its EXIF carries no author or licence
tag — so the public-domain claim could not be evidenced to the SOP
standard ("only clearly public-domain/CC0, credit from the Commons API
Artist field"). Fix route (b) was taken: the file was replaced with the
Washington team photo already verified in the W43 Korean build's CREDITS
(SHA-256 18ad8ae06fac2860d2c03323efd7ad5736de8597e1540058e830ccd35bad1009,
1024×743), whose Commons page, author (Bain News Service) and public-domain
status are recorded above. The P4 caption was reworded to match the new
subject ("棒球舊照(資料照片)") and its credit line to "Photo: Bain News
Service — Public domain (Wikimedia Commons)"; geometry (x, y, w, h) and
the series box below are unchanged. The unverified batter file is NOT
shipped in this edition; a backup copy of the pre-fix file is kept only
at /tmp/zhtw-baseball-orig.jpg for audit, not in the build assets.
