import helper

def get_config(organization, common_args):
    api_results = {
        'GITHUB_INFO': helper.get_latest_github_release_no_browser_download('tomnomnom/httprobe')
    }
    
    config = {
        'name': organization+'/httprobe',
        'version': api_results['GITHUB_INFO']['version'][1:],
        'buildargs': {
            'GOLANG_ALPINE_VERSION': common_args['GOLANG_ALPINE_VERSION'],
            'LATEST_ALPINE_VERSION': common_args['LATEST_ALPINE_VERSION'],
        },
        'tests': ['--help']
    }
    return config