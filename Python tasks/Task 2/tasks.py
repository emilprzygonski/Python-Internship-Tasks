import argparse
import csv
import datetime
import os
import pandas

def refresh_indexes(df):
    df2 = df.reset_index()
    df2 = df2.drop(['index'], axis=1)
    return df2

def main():
    global hash
    parser = argparse.ArgumentParser(description='Task manager')

    subparsers = parser.add_subparsers(title='Actions', dest='command')

    parser_add = subparsers.add_parser("add", add_help=False,
                                       description='Add task',
                                       help='Add some task')
    parser_add.add_argument('--name', type=str, required=True)
    parser_add.add_argument('--deadline', type=datetime.datetime.fromisoformat, required=False)
    parser_add.add_argument('--description', type=str, required=False)

    parser_update = subparsers.add_parser("update", add_help=False,
                                          description='Update task',
                                          help='Update some task')
    parser_update.add_argument('--name', type=str, required=False)
    parser_update.add_argument('--deadline', type=datetime.datetime.fromisoformat, required=False)
    parser_update.add_argument('--description', type=str, required=False)
    parser_update.add_argument('integers', type=int, help='an id')

    parser_remove = subparsers.add_parser("remove")
    parser_remove.add_argument('integers', type=int, help='an id')

    parser_list = subparsers.add_parser("list")
    group = parser_list.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true')
    group.add_argument('--today', action='store_true')

    args = vars(parser.parse_args())

    value = list(args.values())[1:]

    with open('tasks.csv', 'a') as f:  # Just use 'w' mode in 3.x
        if os.stat("tasks.csv").st_size == 0:
            writer = csv.writer(f)
            writer.writerow(['name', 'deadline', 'description', 'hash'])
        else:
            pass
    df = pandas.read_csv('tasks.csv', index_col=0)

    if args['command'] == 'add':
        del args['command']
        hash_number = hash(frozenset(args.items()))
        args['hash'] = hash_number

        df2 = pandas.DataFrame.from_records([args])

        df = df.append(df2, ignore_index=True)
        df.to_csv('tasks.csv')

    elif args['command'] == 'update':
        # hash = args['integers']
        idx = df[df['hash'] == [args['integers']][0]].index.values

        name = args['name']
        date = args['deadline']
        description = args['description']

        if name != None:
            # df['name'][idx] = name
            df.iloc[idx, df.columns.get_loc('name')] = name
        if date != None:
            # df['deadline'][idx] = date
            df.iloc[idx, df.columns.get_loc('deadline')] = date
        if description != None:
            # df['description'][idx] = description
            df.iloc[idx, df.columns.get_loc('description')] = description

        df = refresh_indexes(df)
        df.to_csv('tasks.csv')

    #
    #
    elif args['command'] == 'remove':
        # print('dupa')
        # print([args['integers']][0])
        print(args)
        idx = df[df['hash'] == [args['integers']][0]].index.values
        print(idx)
        df.drop(df.index[idx], inplace=True)
        df = refresh_indexes(df)
        df.to_csv('tasks.csv')
        print(df)

    elif args['command'] == 'list':
        df = refresh_indexes(df)
        if args['all']:
            print(df)
        else:
            for i in range(len(df.deadline)):
                date = datetime.datetime.strptime(df['deadline'][i], "%Y-%m-%d %H:%M:%S")
                if date.date() == datetime.date.today():
                    print(df.iloc[[i]])
                else:
                    pass

    # print(args)


if __name__ == '__main__':
    main()
