####  我的期中作業是使用RVC變聲器去復刻與重現包含胡璉將軍、遊戲《崩壞:星瓊鐵道》角色卡芙卡等等人物的聲音
它的原理流程1.特徵提取 2.音高提取 3.建立檢索INDEX 4.VITS聲音合成模型 5.聲音推理  

首先我下載了開源軟體[RVC](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)，使用一件安裝的懶人包完成環境設置。接著處理收集相關的聲音資料集的wav/mp3檔案，使用RVC本身的降躁功能把聲音變乾淨後就開始進行訓練，我讓它進行一千輪的訓練，
過程中卻發現loss_kl 無限接近於0，我一查才知道是素材太少(十分鐘語音)輪數太多導致了過擬和發生，於是我增加了訓練資料數量，減少訓練輪次至200輪，最後成功把模型處理好。  
得到模型後，我下載了一首歌曲(轉身即心痛)[https://www.youtube.com/watch?v=8lXzbURdez0]
，用RVC進行人聲分離，再把vocal進行模，把背景音跟推理結果放進去Audacity對齊音軌，最後用Adobe Photoshop把角色圖片上封面圖、說明等等的操作，部分使用Adobe Premiere PRO剪輯、Acytime上字幕軟體。我嘗試讓AI翻唱六首歌曲，
最後完成了三首歌(因為人聲分離乾淨程度、男女對唱較難實現翻唱等等原因)[轉身即心痛](https://youtu.be/m-rEMpnIkXg), [星間旅行](https://youtube.com/shorts/I-YZPzYV7qU?feature=share), [アイドル](https://youtu.be/m-rEMpnIkXg)  

常見數值: loss_total:模型整體學習誤差的加總, loss_fm:音頻特徵之間的匹配誤差, loss_mel:預測的 Mel 頻譜與真實語音 Mel 頻譜之間的差距, loss_dur:音素時長預測的誤差（若使用 VITS 結合時長模型）, 
loss_kl: Variational Autoencoder（VAE）中衡量潛在變數分布與真實分布差距的誤差, loss_d:判別器（Discriminator）在判斷真假音頻的損失, loss_g:生成器（Generator）在欺騙判別器時的損失  

成果與反思:上傳至YT後，兩天內獲得了三則留言十個讚，117、171、215次觀看。結果是曝光不足，我自己認為蠻可惜的，從做影片受眾來看，之前有傳過使用RVC分離人聲的[卡芙卡PV影片](https://youtu.be/Bvq3QC7V8Go)獲得了近12,000次觀看，一百多讚，從這點可以確認中文受眾的族群是足夠的，成功的話甚至能有幾十幾百萬觀看，比如[老高](https://www.youtube.com/@laogao)，[小Lin說](https://www.youtube.com/@xiao_lin_shuo)等等
