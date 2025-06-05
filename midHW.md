####  我的期中作業是使用RVC變聲器去復刻與重現包含胡璉將軍、遊戲《崩壞:星瓊鐵道》角色卡芙卡等等人物的聲音
首先我下載了開源軟體[RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)，然後處理收集相關的聲音資料集的wav/mp3檔案，使用RVC本身的降躁功能把聲音變乾淨，之後開始進行訓練，我讓它進行一千輪的訓練，
過程中卻發現loss_kl無限接近於0，我一查才知道是素材太少(十分鐘語音)輪數太多導致過擬和，於是我增加了訓練資料數量，減少訓練輪次至200輪，最後成功把模型處理好。  
得到模型後，我下載了一首歌曲(轉身即心痛)[https://www.youtube.com/watch?v=8lXzbURdez0]
，用RVC進行人聲分離，再把vocal進行模，把背景音跟推理結果放進去Audacity對齊音軌，最後用Adobe Photoshop把角色圖片上封面圖、說明等等的操作，部分使用Adobe Premiere PRO剪輯、Acytime上字幕軟體。我嘗試讓AI翻唱六首歌曲，
最後完成了三首歌(因為人聲分離乾淨程度、男女對唱較難實現翻唱等等原因)  

常見數值: loss_total:模型整體學習誤差的加總, loss_fm:音頻特徵之間的匹配誤差, loss_mel:預測的 Mel 頻譜與真實語音 Mel 頻譜之間的差距, loss_dur:音素時長預測的誤差（若使用 VITS 結合時長模型）, 
loss_kl: Variational Autoencoder（VAE）中衡量潛在變數分布與真實分布差距的誤差, loss_d:判別器（Discriminator）在判斷真假音頻的損失, loss_g:生成器（Generator）在欺騙判別器時的損失  

