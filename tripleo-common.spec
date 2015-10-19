%global commit0 fbb29e3a5a9fa4349e14d78ae0c8417a53cbf3ff
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%{!?upstream_version: %global upstream_version %{version}}

%{?!_licensedir:%global license %%doc}

Name:           tripleo-common
Summary:        Python library for code used by TripleO projects.
Version:        0.0.1
Release:        2%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://github.com/rdo-management/tripleo-common

# Once we have stable branches and stable releases we can go back to using release tarballs
Source0:  https://github.com/openstack/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-heatclient


%prep
%autosetup -n %{name}-%{commit0} -S git
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%description
Python library for code used by TripleO projects.

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/tripleo_common*
%exclude %{python2_sitelib}/tripleo_common/test*


%changelog
* Mon Oct 19 2015 John Trowbridge <trown@redhat.com> - 0.0.1-2
- Use a source tarball for a git hash that has passed delorean CI for liberty release

* Wed Apr 15 2015 Jan Provaznik <jprovazn@redhat.com> - 0.0.1-1
- Initial package build

