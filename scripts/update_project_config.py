import os
import sys
import commands
import shutil
import subprocess
from optparse import OptionParser


def usage():
    usage_string = """

    ***** USAGE *****
    usage: ./update_project_config.py -n my-custom-project -p organization -pid 234672775 -b 21341235
    use ./update_project_config.py --help for details
    *****************
    """
    sys.stdout.write(usage_string)

# Program's Entry Point
if __name__ == '__main__':
    # Set command line options -j for jobname, -b for buildnumber
    parser = OptionParser()
    parser.add_option("-n", "--project-name", action="store", type="string", dest="project_name", help="Unique Project Name", default=False)
    parser.add_option("-p", "--parent-type", action="store", type="string", dest="parent_type", help="parent for the Project organization/folder", default="organization")
    # parser.add_option("-pid", "--parent-id", action="store", type="string", dest="parent_id", help="ID of the parent:organization ID or folder ID", default=False)
    parser.add_option("-b", "--billing-account-id", action="store", type="string", dest="billing_account_id", help="Billing Account ID associated with the Project",default=False)

    (options, args) = parser.parse_args()
    # validate if passed options are valid ones
    if not options.project_name:
        sys.stdout.write('ERROR: missing arg -p (--project-name) \n')
        usage
        sys.exit(1)
    else:
        project_name = options.project_name

    if not options.parent_id:
        sys.stdout.write('ERROR: missing arg -pid (--parent-id) \n')
        usage
        sys.exit(1)
    else:
        parent_id = options.parent_id

    if not options.billing_account_id:
        sys.stdout.write('ERROR: missing arg -b (--billing-account-id) \n')
        usage
        sys.exit(1)
    else:
        billing_account_id = options.billing_account_id


    # # os.system('source ../cft-env-vars')
    # #print os.environ
    # stream = file('../project/project.yaml', 'r')
    # project_config = yaml.load(stream)

    # project_config['resources'][0]['name'] = 'sourced-cft-demo-0'
    # print project_config['resources'][0]