import os
import os.path as op


class DirectoryWorking:
    """Class to realize files renaming logic"""

    @staticmethod
    def __get_dir_files(dir_path: str) -> list[str] | None:
        """Private method to get list of file paths in given directory"""
        files = [op.join(dp, f) for (dp, dn, filenames) in os.walk(dir_path) if dp == dir_path for f in filenames]

        return files

    @staticmethod
    def get_curr_dir() -> str:
        """Method to get current path where program has been started"""
        return os.getcwd()

    @staticmethod
    def renaming_files_in_dir(dir_path: str, begin_num: int = 1, prefix: str = '', delimiter: str = '.') -> bool:
        """Method to rename files in specified directory according to given sequence parameters.
        User may specify prefix and delimiter for renaming"""
        files = DirectoryWorking.__get_dir_files(dir_path)

        if files is not None:

            file_num = begin_num
            if prefix == '':
                pr_delim = ''
            else:
                pr_delim = delimiter

            for fl in files:
                print('Renaming file: ' + fl)
                new_fname = op.join(dir_path,
                                    prefix + pr_delim + str(file_num).zfill(2) + delimiter + fl.split('/')[-1])
                os.rename(fl, new_fname)
                file_num += 1

            return True

        else:
            print('Nothing to do in this directory')
            return False

    @staticmethod
    def undo_renaming_in_dir(dir_path: str, prefix: str = '', delimiter: str = '.') -> bool:
        """Method to undo previous sequence renaming in current directory"""
        files = DirectoryWorking.__get_dir_files(dir_path)

        if files is not None:
            for fl in files:
                print('Working with file: ' + fl)
                new_name = fl.split('/')[-1]

                if len(fl.split('.')) < 2 or len(fl.split(delimiter)) < 2:
                    print('Skipping this file')
                    continue
                elif prefix != '':
                    new_name = new_name.removeprefix(prefix + delimiter)

                if len(new_name.split(delimiter)) > 1:
                    new_name = ''.join(new_name.split(delimiter)[1:])

                new_filename = op.join(dir_path, new_name)
                os.rename(fl, new_filename)

            return True

        else:
            print('Nothing to do in this directory')
            return False
