# toads-and-frogs
Toads and Frogs combinatorial game by Richard Guy

    p_w_l(1)
        [0, 3, 0]
    p_w_l(2)
        [1, 8, 0]
    p_w_l(3)
        [6, 21, 0]
    p_w_l(4)
        [24, 57, 0]
    p_w_l(5)
        [86, 156, 1]
    p_w_l(6)
        [277, 430, 22]
    p_w_l(7)
        [835, 1177, 175]
    p_w_l(8)
        [2433, 3218, 910]
    p_w_l(9)
        [6923, 8777, 3983]
    p_w_l(10)
        [19404, 23922, 15723]


    p_win(1)
        [0.0, 1.0]
    p_win(2)
        [0.1111111111111111, 0.8888888888888888]
    p_win(3)
        [0.2222222222222222, 0.7777777777777778]
    p_win(4)
        [0.2962962962962963, 0.7037037037037037]
    p_win(5)
        [0.35699588477366256, 0.6430041152263375]
    p_win(6)
        [0.39701206429601493, 0.6029879357039851]
    p_win(7)
        [0.4246315790372863, 0.5753684209627136]
    p_win(8)
        [0.4438821042360025, 0.5561178957639971]
    p_win(9)
        [0.45690660291722374, 0.5430933970827762]
    p_win(10)
        [0.465558723347825, 0.5344412766521747]


    p_fair(6)
        {' FTT F', 'T FTF ', 'TF FT ', ' T T F', 'TF  TF'}
    p_fair(7)
        {'FTF  TF', 'T F F  ', ' FT F  ', 'T FTF F', 'FT FTF ', '  TTF  ', '  T TF ', 'F FTT F', '  TF T ', ' TFTTF ', 'TFT T F', 'TF  TFT', '  T T F', 'T FTFT ', ' T T FT', 'F T T F', ' FTT FT', '  TT  F', ' T FFT ', 'T TFTF ', ' T FF  ', 'TF FT T', 'T FTF T', ' FTTT F', 'FTF FT ', 'TF FFT '}
    p_fair(8)
        {'T F F   ', ' FTTTT F', 'T FFFFT ', 'TF FFT T', 'FFTF  TF', ' T T FTT', ' TFTFTF ', ' TFFTFT ', 'T F F  T', 'TF FT F ', ' T FFT T', ' TFTTF T', 'T FTF TT', '  TTF  T', '  T TF T', '   TF T ', '  TT  FT', '  T T FT', ' FT F  T', 'TF T TFF', 'T  FTTF ', 'FT F F  ', '  TFT F ', '  TF T T', 'FT FTFT ', 'TF FFFT ', ' TF TF  ', 'F  TTF  ', 'F FTT FT', 'T FTF FT', 'F T FF  ', 'FTF FFT ', 'FFT FTF ', 'FTF  TFT', 'F  TT  F', ' TTF F  ', ' FTTT FT', 'F  T T F', 'T TTT FF', 'T FTFT T', 'TFTF FT ', 'F TFTTF ', 'F  T TF ', 'FT FTF F', 'FT FTF T', 'FF T T F', 'F T T FT', 'F FT F  ', 'TF FT TT', 'FTF FT T', ' T FF   ', '   T TF ', 'TF  TFTF', 'FT TFTF ', ' FTT FTT', ' FTFTTF ', 'T TFFTF ', 'FF FTT F', 'T TFTF T', 'TF FF T ', 'TFT T FT', ' FTT FTF', 'FTFT T F', 'TF  TFTT', '   TT  F', 'F FTTT F', ' F TTT F', 'F T FFT ', ' T  TFF ', ' FT F   ', ' TTF  TF', 'TF FFT F', 'FFTF FT ', '  TFF T ', 'F  TF T ', '  TT FF ', ' T FF  T', '   TTF  '}
    p_fair(9):
        {'T TFF FT ', 'F T FF  T', ' FTT FTTT', 'FFT FTF F', 'FT TFFTF ', ' T TTT FF', 'FF  TF T ', 'FFT FTF T', 'FFT FTFT ', 'TTF TT TF', '  T T FTT', 'T TFTF TT', 'FFTF  TFT', 'FFTF FT T', 'TF TT TFF', 'TF T TFFT', 'T F F   T', 'T T FTFF ', 'FT FTF TT', 'T FTFTFT ', 'FFFTF  TF', 'F   TF T ', ' TFTT FF ', ' TTTF TF ', 'TFTF  TFF', '  TT FF T', 'FF  T TF ', 'T TTT FFT', '    TT  F', '  FTT   F', 'F TFTTF T', 'T FTF TTT', 'TFFTF FT ', 'F TFFTFT ', ' FT F   T', 'T TFTTTF ', ' TFFTFTT ', ' FTFTTFT ', 'FTF FFT F', 'TF FFFT T', 'TTF FT TF', 'TFT TFTF ', 'F   TT  F', ' TFFTFT T', ' FTTFTT F', 'FT TTT FF', 'FF FT F  ', 'TF  TFTTT', 'FFT F F  ', 'F FTTT FT', '    T TF ', 'TFFTF  TF', ' TFTTF TT', 'F  T TF T', '  TFF T T', 'FF FTTT F', 'TFT FTFT ', 'FT FTFT T', 'F T FFT T', 'FF  TTF  ', ' FF TFT  ', '  T TF TF', '  TTF  TT', 'TT FTFF F', 'T FFFFT T', ' FTTTTTF ', ' TFTFTF T', ' FT F  TT', ' T T FTTT', 'F FTFTTF ', 'TF FFFFT ', 'TF  TFTFF', 'F FTTTT F', '  TFF  T ', 'TFT T FTT', 'FFF FTT F', ' TT FFFF ', 'F  TFF T ', ' F TTT FT', 'FT F F   ', 'FTF FFT T', '   T TF T', 'T T TFF F', 'F   T TF ', 'FT FFFFT ', 'F  TTF  T', ' TTTTF F ', ' FTTTT FT', ' FTT FTFT', ' FT   F  ', 'FFT TFTF ', '   TF T T', 'TF FFT TT', 'F TTF F  ', 'T FTF FTT', 'FT TFTF T', 'FFTF FFT ', ' F TF TT ', 'FF  T T F', 'T  FTTF T', 'TFTF FFT ', 'TTFTF FT ', ' F  TTT F', '  TFT F T', 'T F F    ', 'FT F F  T', 'FF T T FT', 'FF  TT  F', 'F FTT FTF', ' TF TF  T', ' TF  FTT ', 'F  T T FT', 'TFTF TT F', 'TFT F F  ', 'TF FF T T', 'T  TFFFF ', 'F  TT  FT', 'T FFTFFT ', 'FF T FF  ', 'F  TFT F ', 'T FFTT FF', ' TFTFTFT ', ' TFTTFTF ', ' FT T TFF', '  T TF TT', 'FTF FF T ', 'T FTF FTF', ' FTFTTF F', 'T FTFT TF', 'FTF  TFTF', 'F TFTFTF ', 'T F F  TT', ' TFF TF  ', 'TFF FTT F', 'T FFFF T ', ' TTF FTF ', '   TTF  T', '   TT  FT', 'TFTF FT T', 'TFFT FTF ', 'T  F FT  ', 'TF  TFTTF', 'FTFT T FT', 'F TF TF  ', 'F T FF   ', 'FT FTF FT', ' FTTTTT F', 'TF FF  T ', 'FF T FFT ', ' T T FTTF', ' FTT FTTF', 'T TTTT FF', 'TF FT TTT', ' FT  TTF ', 'F FTT FTT', ' TFTF FT ', 'FTF  TFTT', 'F  TT FF ', 'T TFFTF T', 'T FTF TTF', 'T FFTTT F', ' TFTTF TF', 'TF FTFFT ', 'TF TT FTF', '  T  F T ', 'TFF T T F', 'F T T FTT', 'T FTFT TT', ' T FF  TT', 'FFFTF FT ', 'T F TFFF ', ' T FFT TT', 'T TTFTF F', 'FFF T T F', 'F FT F  T', 'F  TF T T', ' TTTFT  F', ' FTTT FTF', 'F T  TFF ', 'TF FT TTF', ' TFT FFF ', 'T FTFTTF ', 'FF TFTTF ', ' TTF F  T', ' FTT FTFF', 'FTF FT TT', ' FTFTTF T', 'TF FFT FT', 'TT TFFTF ', 'F FT F   ', 'FTF FT F ', 'TTTF FF F', 'TTT FFT F', ' T  TFF T', 'FTF FFFT ', 'FFTFT T F', 'F F TTT F', ' T FF   T', '  TT  FTF', ' TTF  TFT', ' TF   TF ', 'FF FTT FT', 'F   TTF  ', 'TF  TTT F', 'FT  FTTF ', 'F TTF  TF', ' F TTTT F', '  TF T TT', '  TT  FTT', ' FTTT FTT', 'TFTFT T F', ' TFTFTF F', 'TF  TFTFT', 'FTFTF FT ', 'FTF T TFF', 'TF FT F T', 'T TTFT FF', 'FFFT FTF ', 'TF FFF T ', 'T TFTF TF', 'TT FFFFT '}
