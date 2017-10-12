%define         ros_distro kinetic
%define         ros_root /opt/ros
%define         install_path %{ros_root}/%{ros_distro}
%define         sub_pkg_path %{nil}

Name:           ros-kinetic-std-msgs
Version:        0.5.11
Release:        0%{?dist}
Summary:        ROS std_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/std_msgs
Source0:        %{name}-%{version}.tar.gz
Source1:        cmake_manifest_parser
Source1001:     %{name}.manifest

BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-gencpp
BuildRequires:  ros-kinetic-geneus
BuildRequires:  ros-kinetic-genlisp
BuildRequires:  ros-kinetic-genpy
BuildRequires:  ros-kinetic-gennodejs
Requires:       ros-kinetic-message-runtime

%description
Standard ROS Messages including common message types representing primitive data
types and other basic message constructs, such as multiarrays. For common,
generic robot-specific message types, please see common_msgs.

%prep
%setup -q
cp %{SOURCE1001} .

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="%{install_path}" \
        -DCMAKE_PREFIX_PATH="%{install_path}" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd build
make install DESTDIR=%{buildroot}
popd
python %{SOURCE1} %{buildroot}

%files -f ros_install_manifest
%manifest %{name}.manifest
