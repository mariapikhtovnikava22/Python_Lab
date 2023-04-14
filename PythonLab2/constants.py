Abbreviate = r"\b(Mrs?\.|Ms\.|Ave\.|Sq\.|Rd\.|Bldg\.|B\.|Sc\.|M\.D\.|Ph\.D\.|Rep\.|Dr\.|Lt\.|St\.|Blvd\.)"

other_abbreviate = r"\b\d?(i\.e|e\.g\.|etc\.|p\.a\.|a\.m\.|p\.m\.|P\.S\.|Re\.|p\.|" + \
                   r"exp\.|err\.|et\.al\.|ex\.|fin\.|vs\.|N\.B\.|" + \
                   r"ft\.|oz\.|pt\.|in\.|sec\.|g\.|cm\.|qt\.|" + \
                   r"Jan\.|Feb\.|Aug\.|Sept\.|Oct\.|Nov\.|Dec\.|Sun\.|" + \
                   r"Mon\.|Tues\.|Wed\.|Thurs\.|Fri\.|Sat.\|Sun\.|" + \
                   r"\.com|\.ru|\.by|\.cpp|\.cs|\.txt|\.py)(?!\s+[A-Z])"

ThreeSigns = r"(\.\s*(?!\n)|\!\s*(?!\n)|\?\s*){3}\b"

numbers_pattern = r"\b\d+(\.)\d+\b"

word_pattern = r"\b\d*\w+\d*\w*\b"

direct_speech_pat = r'"([^"]*)"'
