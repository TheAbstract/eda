'Given the outcomes and predictions of a model, uses the ROC library to compute the auc.'
auc <- function(outcomes, predictions) {
  as.numeric(performance(prediction(predictions, outcomes), "auc")@y.values)
}

'Given the outcomes and predictions of a model, uses the ROCR library to plot the ROC.'
plot_roc <- function(outcomes, predictions){
  ROC <- performance(prediction(predictions, outcomes), 'tpr', 'fpr')
  plot(ROC, colorize=TRUE, print.cutoffs.at=seq(0, 1, 0.1), text.adj=c(-0.2, 1.7))
}
