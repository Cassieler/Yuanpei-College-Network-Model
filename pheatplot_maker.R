##载入程辑包
library(haven)
library(ggplot2)
library(ggcorrplot)

##绘制相关性图
data <- read_sav(".../相关矩阵.sav")
rownames(data)<-colnames(data)
ggcorrplot(data, method = c("square"), type = c("full"), ggtheme = ggplot2::theme_void, title = " ", show.legend = TRUE, show.diag = T, outline.color = "white", hc.order = F, hc.method = "single", lab = F, lab_col = "black", lab_size = 2, p.mat = NULL, sig.level = 0.05, insig = c("pch"), pch = 4, pch.col = "white", pch.cex = 4.5, tl.cex = 6, tl.col = "black", tl.srt = 45, digits = 2)

##绘制相关性图显著部分
reliance <- read_sav(".../相关显著性矩阵.sav")
pmat<-reliance
rownames(pmat)<-colnames(pmat)
for(i in 1:28)(pmat[i,i]=0.00e+28)
pmate<-as.matrix(pmat)
ggcorrplot(data, method = c("square"), type = c("full"), ggtheme = ggplot2::theme_void, title = " ", show.legend = TRUE, show.diag = T, outline.color = "white", hc.order = F, hc.method = "single", lab = F, lab_col = "black", lab_size = 2, p.mat = pmate, sig.level = 0.05, insig = "blank", tl.cex = 6, tl.col = "black", tl.srt = 45, digits = 2)