import numpy as np

def single_figure_plot(plt, df, cols, title='Stock prices', xlabel = 'Time (days)', ylabel = 'Price (Dollar)'):
    
    #plt.figure(figsize)
    for col in cols:
        plt.plot(df[col[0]], color=col[1], label=[col[0]])
    
    plt.set_title(title)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    plt.legend(loc='best')
    return plt

def multiple_plots(axes, df, fig_dict = []):
    '''
    {
        'col':'',
        'color': '',
        'label': '',
        'title': '',
        'xlabel': '',
        'ylabel': ''
    }
    '''
    nplots = len(fig_dict)
    i = 0
    for ax in axes:
        if i == nplots:
            break

        fig = fig_dict[i]
        ax.plot(df[fig['col']], color=fig['color'], label=fig['label'])
        ax.set_xlabel(fig['xlabel'])
        ax.set_ylabel(fig['ylabel'])
        ax.set_title(fig['title'])
        i += 1


def plot_predictions(axes, data):
    #plt.figure(figsize=(15, 5))
    #plt.subplot(1,2,1);
    ft = 0
    y_train = data[1]
    y_valid = data[3]
    y_test = data[5]
    y_train_pred = data[6]
    y_test_pred = data[7]
    y_valid_pred = data[8]

    axes[0].plot(np.arange(y_train.shape[0]), y_train[:,ft], color='blue', label='train target')

    axes[0].plot(np.arange(y_train.shape[0], y_train.shape[0]+y_valid.shape[0]), y_valid[:,ft],
            color='gray', label='valid target')

    axes[0].plot(np.arange(y_train.shape[0]+y_valid.shape[0],
                    y_train.shape[0]+y_test.shape[0]+y_test.shape[0]),
            y_test[:,ft], color='black', label='test target')

    axes[0].plot(np.arange(y_train_pred.shape[0]),y_train_pred[:,ft], color='red',
            label='train prediction')

    axes[0].plot(np.arange(y_train_pred.shape[0], y_train_pred.shape[0]+y_valid_pred.shape[0]),
            y_valid_pred[:,ft], color='orange', label='valid prediction')

    axes[0].plot(np.arange(y_train_pred.shape[0]+y_valid_pred.shape[0],
                    y_train_pred.shape[0]+y_valid_pred.shape[0]+y_test_pred.shape[0]),
            y_test_pred[:,ft], color='green', label='test prediction')

    axes[0].set_title('Historical and predicted stock prices')
    axes[0].set_xlabel('Time [days]')
    axes[0].set_ylabel('Normalized Price')
    axes[0].legend(loc='best');

    #plt.subplot(1,2,2);

    axes[1].plot(np.arange(y_train.shape[0], y_train.shape[0]+y_test.shape[0]),
            y_test[:,ft], color='black', label='test target')

    axes[1].plot(np.arange(y_train_pred.shape[0], y_train_pred.shape[0]+y_test_pred.shape[0]),
            y_test_pred[:,ft], color='green', label='test prediction')

    axes[1].set_title('Forecasted stock price')
    axes[1].set_xlabel('Time [days]')
    axes[1].set_ylabel('Normalized price')
    axes[1].legend(loc='best')
