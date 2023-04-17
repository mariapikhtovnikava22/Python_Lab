Abbreviate = r"\b(Mrs?\.|Ms\.|Ave\.|Sq\.|Rd\.|Bldg\.|B\.|Sc\.|M\.D\.|Ph\.D\.|Rep\.|Dr\.|Lt\.|St\.|Blvd\.)"

other_abbreviate = r"\b\d{,2}(i\.e|e\.g\.|etc\.|ect\.|p\.a\.|a\.m\.|p\.m\.|P\.S\.|Re\.|p\.|" + \
                   r"exp\.|err\.|et\.al\.|ex\.|fin\.|vs\.|N\.B\.|" + \
                   r"ft\.|oz\.|pt\.|in\.|sec\.|g\.|cm\.|qt\.|" + \
                   r"Jan\.|Feb\.|Aug\.|Sept\.|Oct\.|Nov\.|Dec\.|Sun\.|" + \
                   r"Mon\.|Tues\.|Wed\.|Thurs\.|Fri\.|Sat.\|Sun\.|" + \
                   r"\.com|\.ru|\.by|\.cpp|\.cs|\.txt|\.py)(?!\s*[A-Z])"

ThreeSigns = r"(\.\s*|\!\s*|\?\s*)+"

numbers_pattern = r"\b\d+(\.)\d+\b"

word_pattern = r"\b\d*[a-zA-Z]+\d*\w*\b"

#direct_speech_pat = r'"([^"]*)"'
