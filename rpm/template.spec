Name:           ros-indigo-rbdl
Version:        2.3.1
Release:        5%{?dist}
Summary:        ROS rbdl package

Group:          Development/Libraries
License:        zlib
URL:            https://bitbucket.org/rbdl/rbdl
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-catkin
BuildRequires:  cmake
BuildRequires:  eigen3-devel

%description
The Rigid Body Dynamics Library from http://rbdl.bitbucket.org

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 15 2014 Isura Ranatunga <isura@ieee.org> - 2.3.1-5
- Autogenerated by Bloom

* Fri Aug 15 2014 Isura Ranatunga <isura@ieee.org> - 2.3.1-4
- Autogenerated by Bloom

* Fri Aug 15 2014 Isura Ranatunga <isura@ieee.org> - 2.3.1-2
- Autogenerated by Bloom

* Fri Aug 15 2014 Isura Ranatunga <isura@ieee.org> - 2.3.1-3
- Autogenerated by Bloom

