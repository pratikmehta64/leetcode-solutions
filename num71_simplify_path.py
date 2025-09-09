class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        for idx, substr in enumerate(path.split('/')):
            if substr == '..':
                if stack:
                    stack.pop()
                continue
            if substr == '.':
                continue
            if '/' in substr and len(set(list(substr))) == 1:
                continue
            if substr == '':
                continue
            else:
                stack.append(substr)
        if not stack:
            return '/'
        canon_path = '/'.join(stack)
        if canon_path[0] != '/':
            canon_path = '/' + canon_path
        canon_path = canon_path.replace('//', '/')
        return canon_path