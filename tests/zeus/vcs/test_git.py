path = '%s/clone' % (root, )
remote_path = '%s/remote' % (root, )
url = 'file://%s' % (remote_path, )
    check_call(
        'cd {0} && git config --replace-all "user.name" "{1}"'.format(remote_path, name),
        shell=True
    )
    check_call(
        'cd {0} && git config --replace-all "user.email" "{1}"'.format(remote_path, email),
        shell=True
    )
    check_call('rm -rf %s' % (root, ), shell=True)
    check_call('mkdir -p %s %s' % (path, remote_path), shell=True)
    check_call('git init %s' % (remote_path, ), shell=True)
    check_call(
        'cd %s && touch FOO && git add FOO && git commit -m "test\nlol\n"' % (remote_path, ),
        shell=True
    )
    check_call(
        'cd %s && touch BAR && git add BAR && git commit -m "biz\nbaz\n"' % (remote_path, ),
        shell=True
    )
    check_call('rm -rf %s' % (root, ), shell=True)
    return GitVcs(url=url, path=path)
    check_call(
        'cd %s && touch BAZ && git add BAZ && git commit -m "bazzy"' % remote_path, shell=True
    )
    assert_revision(revisions[0], author='Another Committer <ac@d.not.zm.exist>', message='bazzy')
    assert_revision(revisions[0], author='Another Committer <ac@d.not.zm.exist>', message='bazzy')
    revisions = list(vcs.log(branch=vcs.get_default_revision(), author='Foo'))
    check_call('cd %s && git checkout -b B2' % remote_path, shell=True)
    check_call(
        'cd %s && touch BAZ && git add BAZ && git commit -m "second branch commit"' %
        (remote_path, ),
        shell=True
    )
    check_call('cd %s && git checkout %s' % (remote_path, vcs.get_default_revision(), ), shell=True)
    check_call('cd %s && git checkout -b B3' % remote_path, shell=True)
    check_call(
        'cd %s && touch IPSUM && git add IPSUM && git commit -m "3rd branch"' % (remote_path, ),
        shell=True
    )
    assert_revision(last_rev, message='3rd branch', branches=['B3'])
    assert_revision(previous_rev, message='second branch commit', branches=['B2'])
    assert_revision(revisions[3], message='test', branches=[vcs.get_default_revision(), 'B2', 'B3'])
    assert_revision(revisions[0], message='3rd branch', branches=['B3'])
    assert_revision(revisions[2], message='test', branches=[vcs.get_default_revision(), 'B2', 'B3'])
    check_call('cd %s && git checkout %s' % (remote_path, vcs.get_default_revision(), ), shell=True)
    assert_revision(
        revision, author='Foo Bar <foo@example.com>', message='biz\nbaz\n', subject='biz'
    )
        child_in_question=revisions[0].id, parent_in_question=revisions[1].id
    )
        child_in_question=revisions[1].id, parent_in_question=revisions[0].id
    ) is False
    check_call('cd %s && git checkout -B test_branch' % remote_path, shell=True)