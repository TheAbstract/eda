'Given the outcomes and predictions of a model, uses the ROC library to compute the auc.'
auc <- function(outcomes, predictions) {
  as.numeric(performance(prediction(predictions, outcomes), "auc")@y.values)
}

'Given the outcomes and predictions of a model, uses the ROCR library to plot the ROC.'
plot_roc <- function(outcomes, predictions) {
  ROC = performance(prediction(predictions, outcomes), 'tpr', 'fpr')
  plot(ROC, colorize=TRUE, print.cutoffs.at=seq(0, 1, 0.1), text.adj=c(-0.2, 1.7))
}

'Takes outcomes and predictions from a classifier. 
 Computes the confussion matrix and outputs accuracy, TPR, and TNR.'
accuracy <- function(outcomes, predictions) {
  CM = table(outcomes, predictions)
  TotalAccuracy = (CM[1, 1] + CM[2, 2]) / (CM[2, 1] + CM[2, 2] + CM[1, 1] + CM[1, 2])
  TPR = CM[2, 2] / (CM[2, 1] + CM[2, 2])
  TNR = CM[1, 1] / (CM[1, 1] + CM[1, 2])
  as.data.frame(col.names=c('TotalAccuracy', 'TPR', 'TNR'), list(TotalAccuracy, TPR, TNR))
}
